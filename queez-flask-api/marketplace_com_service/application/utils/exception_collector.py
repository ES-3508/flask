class ExceptionCollector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.is_error = False
            cls._instance.error_list = []
        return cls._instance

    def add_error(self, error):
        self.error_list.append(error)
        self.is_error = True

