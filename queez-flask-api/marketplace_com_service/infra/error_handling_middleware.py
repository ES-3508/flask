
class ErrorHandlingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except ValueError as e:
            response_body = "Error: " + str(e)
            status = "400 Bad Request"
            response_headers = [("Content-Type", "text/plain")]

            start_response(status, response_headers)
            return [response_body.encode()]
