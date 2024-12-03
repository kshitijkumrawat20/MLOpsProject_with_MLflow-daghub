from src.project.config.configuration import ConfiguratuionManager
from src.project.components.data_transformation import DataTransformation
from src.project import logger 
import os
import os

STAGE_NAME = "Data transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    def intiate_data_transformation(self):
        try:
            with open(os.path.join("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config = ConfiguratuionManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config= data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Data validation failed")
        except Exception as e:
                print(e)