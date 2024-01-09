from .....infra.logger import log_exceptions
from .....application.utils.response_object import ResponseObject
from .....application.utils.exception_collector import ExceptionCollector
from .....infrastructure.quary.filter_quary_repository import FilterQueryRepository
# from ..responce_objects.advertisement_responce_object import AdvertisementResponseObject
from .....domain.features.adverticement.valueobjects.id import Id
from ..responce_objects.advertisement_responce_object import AdvertisementResponse
from bson import ObjectId
class AdvertisementQueryService:
    def __init__(self, advertisement_query_repository):
        self.advertisement_query_repository = advertisement_query_repository

    @log_exceptions
    def get_advertisement_by_id(self, advertisement_id):
        
        advertisement = self.advertisement_query_repository.get_advertisement_by_id(advertisement_id)
            
        if advertisement:
            advertisement_response_object = AdvertisementResponse(advertisement)
            
        response_object = ResponseObject(is_error=False)
        response_object.add_payload(advertisement_response_object)

        return response_object
    
    
    

    @log_exceptions
    def get_advertisement_by_filter_id_and_value(self, filter_id, value, customer_id):
        advertisements = self.advertisement_query_repository.get_advertisement_by_filter_id_and_value(filter_id, value, customer_id)
        
        # Convert MongoDB ObjectId to string for each document
        sanitized_advertisements = [
            self.sanitize_advertisement(advertisement) for advertisement in advertisements
        ]

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(sanitized_advertisements)

        return response_object

    def sanitize_advertisement(self, advertisement):
        # Convert ObjectId to string and remove _id field
        sanitized_advertisement = {
            key: str(value) if isinstance(value, ObjectId) else value
            for key, value in advertisement.items() if key != '_id'
        }
        return sanitized_advertisement

    
    
    
    # @log_exceptions
    # def get_all_advertisements(self):
    #     advertisements = self.advertisement_query_service.get_all_advertisements()
    #     advertisement_response_objects = []

    #     for advertisement in advertisements:
    #         advertisement_response_objects.append(AdvertisementResponseObject(
    #             publisher_id=advertisement.publisher_id,
    #             time_period=advertisement.time_period,
    #             is_active=advertisement.is_active,
    #             coordinates=advertisement.coordinates,
    #             add_id=advertisement.add_id,
    #             filter_id=advertisement.filter_id,
    #             filtercategory_id=advertisement.filtercategory_id,
    #             value=advertisement.value,
    #             image_url=advertisement.image_url,
    #             thumbnail_photo=advertisement.thumbnail_photo
    #         ))

    #     response_object = ResponseObject(is_error=False)
    #     response_object.add_payload(advertisement_response_objects)

    #     return response_object
