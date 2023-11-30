from ..infrastructure.db_settings.mongo_database import get_collection
from ..infra.logger import log_exceptions


class MongoDRunner:
    def __init__(self):
        super().__init__()
        
    @log_exceptions
    def save_collection(collection_name,json_data):
      
        if json_data:
            collection = get_collection(collection_name)
            collection.insert_one(json_data)
            return 'JSON object saved successfully in MongoDB.'
        else:
            return 'No JSON object found in the request.'

