from src.project.config.configuration import ConfiguratuionManager
from src.project.components.model_evaluation import ModelEvaluation 
from src.project import logger 
import os

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def intiate_model_evaluation(self):
        try:
            config = ConfiguratuionManager()
            model_evaluation_config= config.get_model_evaluation()
            model_evaluation= ModelEvaluation(config= model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
                print(e)