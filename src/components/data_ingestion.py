import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class FilePathManager:
    train_data_path: str =os.path.join('artifacts','train.csv')
    test_data_path: str =os.path.join('artifacts','test.csv')
    raw_data_path: str =os.path.join('artifacts','raw.csv')

class DataPreparation:
    def __init__(self):
        self.file_paths=FilePathManager()

    def prepare_and_split_data(self):
        logging.info("data ingestion started")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("data successfully loaded")

            os.makedirs(os.path.dirname(self.file_paths.train_data_path),exist_ok=True)

            df.to_csv(self.file_paths.raw_data_path,index=False,header=True)
            logging.info("saved the original data")


            logging.info("train,test split starteed")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.file_paths.train_data_path,index=False,header=True)

            test_set.to_csv(self.file_paths.test_data_path,index=False,header=True)

            logging.info("splitting completed")

            return(self.file_paths.train_data_path,self.file_paths.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    print("step 1:preparation of data")
    data_preparation=DataPreparation()
    train_file_path,test_file_path = data_preparation.prepare_and_split_data()
    print(f"train_date_here:{train_file_path}")
    print(f"test_date_here:{test_file_path}")






    '''# === STAGE 2: DATA TRANSFORMATION ===
    print("\n🔧 STAGE 2: Cleaning and transforming the data...")
    data_cleaner = DataTransformation()  # Create the data cleaning machine
    # Transform both training and testing data (clean it up, make it AI-ready)
    clean_train_data, clean_test_data, _ = data_cleaner.initiate_data_transformation(
        train_file_path,    # Input: path to training data
        test_file_path      # Input: path to testing data
    )
    # Output: clean_train_data and clean_test_data are now ready for AI!

    # === STAGE 3: AI MODEL TRAINING ===
    print("\n🤖 STAGE 3: Training the AI model...")
    ai_trainer = ModelTrainer()  # Create the AI training machine
    # Train the AI model and see how good it is
    model_performance = ai_trainer.initiate_model_trainer(
        clean_train_data,    # Use clean training data to teach the AI
        clean_test_data      # Use clean testing data to quiz the AI
    )
    print(f"🎯 Model Performance Score: {model_performance}")'''
