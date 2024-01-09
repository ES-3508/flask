from dotenv import load_dotenv
from ...infra.logger import log_exceptions
from ...domain.features.adverticement.repositories.i_adverticement_command_repository import IAdvertisementCommandRepository
from ...domain.features.adverticement.aggregates.adverticement import AdvertisementHeader
from ...domain.features.adverticement.aggregates.adverticementpackage import AdvertisementPackage
from ...domain.features.adverticement.aggregates.advertisementdetails import AdvertisementDetails
from ...domain.features.adverticement.aggregates.imageurl import ImageDetails
from ...domain.features.adverticement.aggregates.workflow import WorkflowHistory
from ...domain.features.adverticement.aggregates.customer import Customer
from ..orm_mapper.add_header_mapper import AdvertisementHeader_Orm
from ..orm_mapper.add_detail_mapper import AdvertisementDetails_Orm
from ..orm_mapper.add_pkg_mapper import AdvertisementPackage_Orm
from ..orm_mapper.workflow_mapper import WorkflowHistory_Orm
from ..orm_mapper.customer_mapper import Customer_Orm
from ..orm_mapper.image_mapper import ImageDetails_Orm
from ..db_settings.mysql_database_orm import db_context_orm, Session
from ...infra.mongo_quary_runner import MongoDRunner
from ..orm_mapper.filter_mapper import FilterOrm

load_dotenv()

class AdvertisementCommandRepository(IAdvertisementCommandRepository):
    def __init__(self):
        self.db = db_context_orm
        

    @log_exceptions
    def create_advertisement(self, customer: Customer, advertisement: AdvertisementHeader,
                             package: AdvertisementPackage, details: AdvertisementDetails,
                             image: ImageDetails, history: WorkflowHistory):
        # Start a transaction
        with self.db.begin():
            # Create AdvertisementPackage record
            customer_orm = Customer_Orm(
                name=customer.name,
                sys_user_id=customer.sys_user_id
            )
            self.db.add(customer_orm)
            self.db.flush()

            package_orm = AdvertisementPackage_Orm(
                description=package.description,
                number_of_add=package.number_of_add,
                num_days=package.num_days,
                is_active=package.is_active,
                price=package.price
            )
            self.db.add(package_orm)
            self.db.flush()  # Flush to get the auto-generated ID

            # Create AdvertisementHeader record
            header_orm = AdvertisementHeader_Orm(
                publisher_id=customer_orm.customer_id,
                time_period=advertisement.time_period,
                is_active=advertisement.is_active,
                coordinates=advertisement.coordinates,
                wf_state=advertisement.wf_state_id,
                date=advertisement.date,
                user_id=customer_orm.customer_id,
                package_id=package_orm.package_id  # Use the auto-generated ID
            )
            self.db.add(header_orm)
            self.db.flush()  # Flush to get the auto-generated ID

            # Create AdvertisementDetails record
            details_orm = AdvertisementDetails_Orm(
                add_id=details.add_id,
                filter_id=details.filter_id,
                value=details.value,
                header_id=header_orm.header_id  # Use the auto-generated ID
            )
            self.db.add(details_orm)

            # Create ImageDetails record
            image_orm = ImageDetails_Orm(
                image_url=image.image_url,
                transec_ref_id=header_orm.header_id  # Use the auto-generated ID
            )
            self.db.add(image_orm)

            # Create WorkflowHistory record
            history_orm = WorkflowHistory_Orm(
                transec_ref_id=header_orm.header_id,  # Use the auto-generated ID
                state_id=history.state_id,
                state=history.state,
                transection_type=history.transection_type
            )
            self.db.add(history_orm)

            # Query Filter information based on filter_id
            filter_orm = self.db.query(FilterOrm).filter(FilterOrm.id == details_orm.filter_id).first()

        # Commit the transaction
        self.db.commit()

        # Convert AdvertisementHeader object to JSON
        advertisement_json = {
            'header_id': header_orm.header_id,
            'publisher_id': header_orm.publisher_id,
            'time_period': header_orm.time_period,
            'is_active': header_orm.is_active,
            'coordinates': header_orm.coordinates,
            'wf_state_id': header_orm.wf_state,
            'date': header_orm.date,
            'user_id': header_orm.user_id,
            'package_id': header_orm.package_id,
            'customer': {
                'customer_id': customer_orm.customer_id,
                'name': customer_orm.name,
                'sys_user_id': customer_orm.sys_user_id
            },
            'advertisement_package': {
                'package_id': package_orm.package_id,
                'description': package_orm.description,
                'number_of_add': package_orm.number_of_add,
                'num_days': package_orm.num_days,
                'is_active': package_orm.is_active,
                'price': package_orm.price
            },
            'advertisement_details': [
                {
                    'advertisement_details_id': detail.advertisement_details_id,
                    'add_id': detail.add_id,
                    'filter_id': detail.filter_id,
                    'value': detail.value,
                    'filter_info': {
                        'id': filter_orm.id,
                        'name': filter_orm.name,
                        'description': filter_orm.description,
                        'ref_id': filter_orm.ref_id,
                        'type': filter_orm.type,
                        'is_active': filter_orm.is_active,
                        'sql_statement': filter_orm.sql_statement
                    }
                }
                for detail in header_orm.advertisement_details
            ],
            'image_details': [
                {
                    'image_details_id': image.image_details_id,
                    'image_url': image.image_url,
                    'transec_ref_id': image.transec_ref_id
                }
                for image in header_orm.image_details
            ],
            'workflow_history': [
                {
                    'workflow_history_id': history_orm.workflow_history_id,
                    'transec_ref_id': history_orm.transec_ref_id,
                    'state_id': history_orm.state_id,
                    'state': history_orm.state,
                    'transection_type': history_orm.transection_type
                }
                for history in header_orm.workflow_history
            ]
        }


        # Save the JSON object to MongoDB
        MongoDRunner.save_collection('advertisement', advertisement_json)

        return {
            'header_id': header_orm.header_id,
            'package_id': package_orm.package_id,
            'details_id': details_orm.advertisement_details_id,
            'image_id': image_orm.image_details_id,
            'history_id': history_orm.workflow_history_id
        }
        # Return the generated IDs or any other relevant information
        # return {
        #     'header_id': header_orm.header_id,
        #     'package_id': package_orm.package_id,
        #     'details_id': details_orm.advertisement_details_id,
        #     'image_id': image_orm.image_details_id,
        #     'history_id': history_orm.workflow_history_id
        # }

    # @log_exceptions
    # def update_advertisement(self, advertisement_id: int, updated_advertisement_data: AdvertisementHeader) -> None:
    #     session = Session()
    #     header_entity = session.query(HeaderTable).filter_by(id=advertisement_id).first()
    #     if header_entity is not None:
    #         header_entity.publisher_id = updated_advertisement_data.publisher_id.Value
    #         header_entity.time_period = updated_advertisement_data.time_period.Value
    #         header_entity.is_active = updated_advertisement_data.is_active.Value
    #         header_entity.x_coordinate = updated_advertisement_data.coordinates.X
    #         header_entity.y_coordinate = updated_advertisement_data.coordinates.Y

    #         detail_entity = header_entity.detail
    #         detail_entity.add_id = updated_advertisement_data.add_id.Value
    #         detail_entity.filter_id = updated_advertisement_data.filter_id.Value
    #         detail_entity.filtercategory_id = updated_advertisement_data.filtercategory_id.Value
    #         detail_entity.value = updated_advertisement_data.value.Content

    #         image_entity = header_entity.image
    #         image_entity.image_url = updated_advertisement_data.image_url.URL
    #         image_entity.thumbnail_photo = updated_advertisement_data.thumbnail_photo.URL

    #         session.commit()
    #     session.close()

    # @log_exceptions
    # def delete_advertisement(self, advertisement_id: int) -> None:
    #     session = Session()
    #     header_entity = session.query(HeaderTable).filter_by(id=advertisement_id).first()
    #     if header_entity is not None:
    #         session.delete(header_entity)
    #         session.commit()
    #     session.close()
