import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion process started")
        try:
            # Load the original dataset
            df = pd.read_csv('notebook\\data\\stud.csv')
            logging.info("Dataset successfully loaded into DataFrame")

            # Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save original data as backup
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Original data saved as backup")

            # Split the data into training and testing sets
            logging.info("Initiating train-test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save split datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)
