from .....infra.logger import log_exceptions
from .....application.utils.response_object import ResponseObject
# from .....application.features.advertisement.responce_objects.advertisement_responce_object import AdvertisementResponseObject
from .....domain.features.adverticement.aggregates.adverticement import AdvertisementHeader
from .....domain.features.adverticement.aggregates.customer import Customer
from .....domain.features.adverticement.aggregates.adverticementpackage import AdvertisementPackage
from .....domain.features.adverticement.aggregates.advertisementdetails import AdvertisementDetails
from .....domain.features.adverticement.aggregates.imageurl import ImageDetails
from .....domain.features.adverticement.aggregates.workflow import WorkflowHistory


class AdvertisementCommandService:
    def __init__(self, advertisement_command_service):
        self.advertisement_command_service = advertisement_command_service
    
    @log_exceptions
    def create_advertisement(self, customer: Customer, advertisement: AdvertisementHeader, package: AdvertisementPackage,
                             details: AdvertisementDetails, image: ImageDetails, history: WorkflowHistory):
        
        result = self.advertisement_command_service.create_advertisement(customer,advertisement, package, details, image, history)
        

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(result)

        return response_object

    # @log_exceptions
    # def update_advertisement(self, advertisement_id, updated_advertisement_data):
    #     # Assuming that self.advertisement_command_service.update_advertisement returns the updated advertisement data
    #     updated_advertisement = self.advertisement_command_service.update_advertisement(advertisement_id, updated_advertisement_data)

    #     advertisement_response_object = AdvertisementResponseObject(
    #         publisher_id=updated_advertisement.publisher_id,
    #         time_period=updated_advertisement.time_period,
    #         is_active=updated_advertisement.is_active,
    #         coordinates=(updated_advertisement.x_coordinate, updated_advertisement.y_coordinate),
    #         add_id=updated_advertisement.detail.add_id,
    #         filter_id=updated_advertisement.detail.filter_id,
    #         filtercategory_id=updated_advertisement.detail.filtercategory_id,
    #         value=updated_advertisement.detail.value,
    #         image_url=updated_advertisement.image.image_url,
    #         thumbnail_photo=updated_advertisement.image.thumbnail_photo
    #     )

    #     response_object = ResponseObject(is_error=False)
    #     response_object.add_payload(advertisement_response_object)

    #     return response_object

    # @log_exceptions
    # def delete_advertisement(self, advertisement_id):
    #     # Assuming that self.advertisement_command_service.delete_advertisement returns a success indicator
    #     success = self.advertisement_command_service.delete_advertisement(advertisement_id)

    #     response_object = ResponseObject(is_error=not success)

    #     return response_object
