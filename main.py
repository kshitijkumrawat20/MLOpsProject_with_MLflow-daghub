from src.project import logger
from src.project.pipeline.data_ingestion import DataIngestionPipeline, STAGE_NAME
from src.project.pipeline.data_validation import DataValidationPipeline, STAGE_NAME as s2
from src.project.pipeline.data_transformation import DataTransformationPipeline, STAGE_NAME as s3
from src.project.pipeline.model_trainer import ModeltrainingPipeline, STAGE_NAME as s4
from src.project.pipeline.model_evaluation import ModelEvaluationPipeline, STAGE_NAME as s5

try: 
        logger.info(f"----------stage {STAGE_NAME} started----------")
        obj = DataIngestionPipeline()
        obj.intiate_data_ingestion()
        logger.info(f"----------stage {STAGE_NAME} completed----------")
        
        
except Exception as e:
        logger.exception(e)
        raise e

try:
        logger.info(f"----------stage {s2} started----------")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f"----------stage {s2} completed----------")                                  
        
except Exception as e:
        logger.exception(e)
        raise e

try:
        logger.info(f"----------stage {s3} started----------")
        obj = DataTransformationPipeline()
        obj.intiate_data_transformation()
        logger.info(f"----------stage {s3} completed----------")
except Exception as e:
        logger.exception(e)
        raise e

try:
        logger.info(f"----------stage {s4} started----------")
        obj = ModeltrainingPipeline()
        obj.initiate_model_training()
        logger.info(f"----------stage {s4} completed----------")
except Exception as e:
        logger.exception(e)
        raise e

try:
        logger.info(f"----------stage {s5} started----------")
        obj = ModelEvaluationPipeline()
        obj.intiate_model_evaluation()
        logger.info(f"----------stage {s5} completed----------")
except Exception as e:
        logger.exception(e)
        raise e
