from ...application.utils.exception_collector import ExceptionCollector
from ...application.utils.response_object  import ResponseObject


class ErrorResponse:
    def __init__(self):
        self.is_error = True

    def add_payload(self):
        responce_object = ResponseObject(False,[])
        responce_object.add_payload([])
        return responce_object
        

