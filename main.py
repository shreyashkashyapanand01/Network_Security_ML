from NETWORK_SECURITY_PROJECT.networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingPipelineconfig=TrainingPipelineConfig()
        dataIngestionconfig=DataIngestionConfig(trainingPipelineconfig)
        data_ingestion = DataIngestion(dataIngestionconfig)
        logging.info("Data injestion Initiated ")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)