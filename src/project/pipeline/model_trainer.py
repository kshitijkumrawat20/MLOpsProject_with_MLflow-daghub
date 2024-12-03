from src.project.config.configuration import ConfiguratuionManager
from src.project.components.model_trainer import ModelTrainer
from src.project import logging

STAGE_NAME = "Model Training stage"
class ModeltrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfiguratuionManager()
        model_trainer_config = config.get_data_ingestion_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()