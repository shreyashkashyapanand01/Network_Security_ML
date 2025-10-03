from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

from networksecurity.components.data_validation import DataValidation


if __name__=='__main__':
    try:
        trainingPipelineconfig=TrainingPipelineConfig()
        dataIngestionconfig=DataIngestionConfig(trainingPipelineconfig)
        data_ingestion = DataIngestion(dataIngestionconfig)
        logging.info("Data injestion Initiated ")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data injestion completed")
        
        data_validataion_config=DataValidationConfig(trainingPipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validataion_config)

        logging.info("initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)