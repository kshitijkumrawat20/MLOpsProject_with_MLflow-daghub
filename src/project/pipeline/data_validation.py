from src.project.config.configuration import ConfiguratuionManager
from src.project.components.data_validation import DataValidation
from src.project import logger 

STAGE_NAME = "Data validation stage"
class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config= ConfiguratuionManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()
        