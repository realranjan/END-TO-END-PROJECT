import sys
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.utils import save_object

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
    
    def initiate_training(self):
        try:
            logging.info("Starting training pipeline")
            
            logging.info("Step 1: Data Ingestion")
            train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()
            
            logging.info("Step 2: Data Transformation")
            train_arr, test_arr, preprocessor_path = self.data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            
            logging.info("Step 3: Model Training")
            model_path = self.model_trainer.initiate_model_trainer(
                train_arr, test_arr
            )
            
            logging.info("Training pipeline completed successfully")
            return {
                "model_path": model_path,
                "preprocessor_path": preprocessor_path,
                "train_data_path": train_data_path,
                "test_data_path": test_data_path
            }
            
        except Exception as e:
            logging.error(f"Training pipeline failed: {str(e)}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        train_pipeline = TrainPipeline()
        results = train_pipeline.initiate_training()
        print("Training completed successfully!")
        print(f"Model saved at: {results['model_path']}")
        print(f"Preprocessor saved at: {results['preprocessor_path']}")
    except Exception as e:
        print(f"Training failed: {str(e)}")
