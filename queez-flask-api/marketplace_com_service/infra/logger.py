import os
import logging
from dotenv import load_dotenv
import datetime
from ..application.utils.exception_collector import ExceptionCollector

# Load environment variables from .env file
load_dotenv('.env')

def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Get the log file path from the .env file
            # log_file_folder = os.getenv('LOG_FILE')
            print(f"An error occurred in {func.__name__}: {str(e)}")  # Print the error message
            log_file_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_logg_file')
            os.makedirs(log_file_folder_path, exist_ok=True)
            
            current_time = datetime.datetime.now()
            time_string = current_time.strftime("%Y%m%d_%H%M%S")
            file_name = f"file_{time_string}.txt"
            file_path = os.path.join(log_file_folder_path, file_name)
            
            # Log the exception to the specified log file
            logging.basicConfig(filename=file_path, level=logging.ERROR)
            logging.error(f"An error occurred in {func.__name__}: {str(e)}")

            result = ExceptionCollector()
            result.add_error(str(e))
            return False
    return wrapper

