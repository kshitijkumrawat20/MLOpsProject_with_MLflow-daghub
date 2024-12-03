from src.project.config.configuration import ConfiguratuionManager
from src.project.components.data_ingest import Data_Ingestion
from src.project import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self): 
        pass
    def intiate_data_ingestion(self):
        config= ConfiguratuionManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Data_Ingestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try: 
        logger.info(f"----------stage {STAGE_NAME} started----------")
        obj = DataIngestionPipeline()
        obj.intiate_data_ingestion()
        logger.info(f"----------stage {STAGE_NAME} completed----------")
        
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    

