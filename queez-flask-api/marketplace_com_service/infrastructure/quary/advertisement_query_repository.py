from dotenv import load_dotenv
from sqlalchemy.orm import joinedload
from ...infra.logger import log_exceptions
from ...domain.features.adverticement.repositories.i_adverticement_query_ropository import IAdvertisementQueryRepository
from ...domain.features.adverticement.aggregates.adverticement import AdvertisementHeader

from ...domain.features.adverticement.aggregates.adverticement import AdvertisementHeader
from ...domain.features.adverticement.aggregates.adverticementpackage import AdvertisementPackage
from ...domain.features.adverticement.aggregates.advertisementdetails import AdvertisementDetails
from ...domain.features.adverticement.aggregates.imageurl import ImageDetails
from ...domain.features.adverticement.aggregates.workflow import WorkflowHistory
from ...domain.features.adverticement.aggregates.customer import Customer
# from ..orm_mapper.header_mapper import HeaderTable
from ..orm_mapper.add_header_mapper import AdvertisementHeader_Orm
from ..orm_mapper.customer_mapper import Customer_Orm
from ..orm_mapper.saved_filters_mapper import CustomerSavedFilters
from ..orm_mapper.add_header_mapper import AdvertisementHeader_Orm
from ..orm_mapper.add_detail_mapper import AdvertisementDetails_Orm
from ..orm_mapper.add_pkg_mapper import AdvertisementPackage_Orm
from ..orm_mapper.workflow_mapper import WorkflowHistory_Orm
from ..orm_mapper.customer_mapper import Customer_Orm
from ..orm_mapper.image_mapper import ImageDetails_Orm
# from ..orm_mapper.detail_mapper import DetailTable
from ..orm_mapper.image_mapper import ImageDetails_Orm
from ..db_settings.mysql_database_orm import db_context_orm
from ..db_settings.mysql_database_orm import Session
from typing import List
from ..db_settings.mongo_database import get_collection
load_dotenv()

class AdvertisementQueryRepository(IAdvertisementQueryRepository):
    def __init__(self):
        self.db = db_context_orm

    
    @log_exceptions
    def get_advertisement_by_filter_id_and_value(self, filter_id, value, customer_id):
        
            # Save the filter_id and value in CustomerSavedFilters
        saved_filter = CustomerSavedFilters(
            customer_id=customer_id,
            filter_id=filter_id,
            value=value
        )
        self.db.add(saved_filter)
        self.db.commit()
       
        query = {
           "$and": [
                {'advertisement_details.filter_id': filter_id},
                {'advertisement_details.value': value}
            ]
            }
        
        # Get the MongoDB collection
        collection = get_collection('advertisement')
        print(f'MongoDB Query: {query}')
        # Execute the query
        result = collection.find(query)

        # Convert the result to a list
        advertisements = list(result)

        return advertisements
    # @log_exceptions
    # def get_advertisement_by_idd(self, advertisement_id: int) -> AdvertisementHeader:
    #     session = Session()
    #     header_entity = session.query(AdvertisementHeader_Orm).filter_by(header_id=advertisement_id).first()
    #     session.close()

    #     if header_entity is not None:
    #         return AdvertisementHeader(
    #             header_id=header_entity.header_id,
    #             publisher_id=header_entity.publisher_id,
    #             time_period=header_entity.time_period,
    #             is_active=header_entity.is_active,
    #             coordinates=header_entity.coordinates,
    #             wf_state_id=header_entity.wf_state,
    #             date=header_entity.date,
    #             user_id=header_entity.user_id,
    #             package_id=header_entity.package_id
    #         )
    #     return None
    
    
    @log_exceptions
    def get_advertisement_by_id(self, advertisement_id: int) -> AdvertisementHeader:
        session = Session()

        try:
            # Query AdvertisementHeader and join related tables
            advertisement_header = (
                session.query(AdvertisementHeader_Orm)
                .filter(AdvertisementHeader_Orm.header_id == advertisement_id)
                .options(
                    joinedload(AdvertisementHeader_Orm.customer),
                    joinedload(AdvertisementHeader_Orm.advertisement_package_r),
                    joinedload(AdvertisementHeader_Orm.advertisement_details),
                    joinedload(AdvertisementHeader_Orm.image_details),
                    joinedload(AdvertisementHeader_Orm.workflow_history)
                )
                .first()
            )

            if advertisement_header:
                # Convert the AdvertisementHeader_Orm to AdvertisementHeader
                advertisement = AdvertisementHeader(
                    header_id=advertisement_header.header_id,
                    publisher_id=advertisement_header.customer.customer_id,
                    time_period=advertisement_header.time_period,
                    is_active=advertisement_header.is_active,
                    coordinates=advertisement_header.coordinates,
                    wf_state_id=advertisement_header.wf_state,
                    date=advertisement_header.date,
                    user_id=advertisement_header.user_id,
                    package_id=advertisement_header.advertisement_package_r.package_id
                )

                # Add related data to AdvertisementHeader
                advertisement.customer = Customer(
                    customer_id=advertisement_header.customer.customer_id,
                    name=advertisement_header.customer.name,
                    sys_user_id=advertisement_header.customer.sys_user_id
                )

                advertisement.advertisement_package = AdvertisementPackage(
                    package_id=advertisement_header.advertisement_package_r.package_id,
                    description=advertisement_header.advertisement_package_r.description,
                    number_of_add=advertisement_header.advertisement_package_r.number_of_add,
                    num_days=advertisement_header.advertisement_package_r.num_days,
                    is_active=advertisement_header.advertisement_package_r.is_active,
                    price=advertisement_header.advertisement_package_r.price
                )

                advertisement.advertisement_details = [
                    AdvertisementDetails(
                        advertisement_details_id=details.advertisement_details_id,
                        add_id=details.add_id,
                        filter_id=details.filter_id,
                        value=details.value
                    )
                    for details in advertisement_header.advertisement_details
                ]

                advertisement.image_details = [
                    ImageDetails(
                        image_details_id=image.image_details_id,
                        image_url=image.image_url,
                        transec_ref_id=image.transec_ref_id
                    )
                    for image in advertisement_header.image_details
                ]

                advertisement.workflow_history = [
                    WorkflowHistory(
                        workflow_history_id=history.workflow_history_id,
                        transec_ref_id=history.transec_ref_id,
                        state_id=history.state_id,
                        state=history.state,
                        transection_type=history.transection_type
                    )
                    for history in advertisement_header.workflow_history
                ]

                return advertisement

        finally:
            session.close()


  
    # @log_exceptions
    # def get_all_advertisements(self) -> List[Advertisement]:
    #     advertisements = (
    #         self.session.query(
    #             HeaderTable.publisher_id,
    #             HeaderTable.time_period,
    #             HeaderTable.is_active,
    #             HeaderTable.x_coordinate,
    #             HeaderTable.y_coordinate,
    #             DetailTable.add_id,
    #             DetailTable.filter_id,
    #             DetailTable.filtercategory_id,
    #             DetailTable.value,
    #             ImageTable.image_url,
    #             ImageTable.thumbnail_photo,
    #         )
    #         .join(DetailTable, HeaderTable.id == DetailTable.add_id)
    #         .join(ImageTable, HeaderTable.id == ImageTable.id)
    #         .all()
    #     )

    #     advertisement_list = [
    #         Advertisement(
    #             publisher_id=row.publisher_id,
    #             time_period=row.time_period,
    #             is_active=row.is_active,
    #             coordinates= row.x_coordinate,
    #             add_id=row.add_id,
    #             filter_id=row.filter_id,
    #             filtercategory_id=row.filtercategory_id,
    #             value=row.value,
    #             image_url=row.image_url,
    #             thumbnail_photo=row.thumbnail_photo,
    #         )
    #         for row in advertisements
    #     ]

    #     return advertisement_list
    
    # @log_exceptions
    # def filter_by_category(self, category: str) -> List[Advertisement]:
    #     header_entities = self.session.query(HeaderTable).filter(HeaderTable.detail.filter.category == category).all()
    #     self.session.close()

    #     advertisements = []
    #     for header_entity in header_entities:
    #         advertisements.append(
    #             Advertisement(
    #                 publisher_id=header_entity.publisher_id,
    #                 time_period=header_entity.time_period,
    #                 is_active=header_entity.is_active,
    #                 coordinates=(header_entity.x_coordinate, header_entity.y_coordinate),
    #                 add_id=header_entity.detail.add_id,
    #                 filter_id=header_entity.detail.filter_id,
    #                 filtercategory_id=header_entity.detail.filtercategory_id,
    #                 value=header_entity.detail.value,
    #                 image_url=header_entity.image.image_url,
    #                 thumbnail_photo=header_entity.image.thumbnail_photo
    #             )
    #         )
    #     return advertisements
    # Add more query methods as needed for your application
