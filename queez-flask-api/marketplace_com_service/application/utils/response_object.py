from ..utils.exception_collector import ExceptionCollector


class ResponseObject:
    def __init__(self, is_error, payload=None):
        self.is_error = is_error
        self.error_list = []
        self.payload = payload

    def add_payload(self, payload):
        self.payload = payload

       