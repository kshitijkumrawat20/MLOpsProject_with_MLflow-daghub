from src.project import logger
from src.project.pipeline.data_ingestion import DataIngestionPipeline, STAGE_NAME

try: 
        logger.info(f"----------stage {STAGE_NAME} started----------")
        obj = DataIngestionPipeline()
        obj.intiate_data_ingestion()
        logger.info(f"----------stage {STAGE_NAME} completed----------")
        
        
except Exception as e:
        logger.exception(e)
        raise e