import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import Datacleaner
from src.components.data_transformation import datacleaning
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
    train_data_path,test_data_path = data_preparation.prepare_and_split_data()
    print(f"train_date_here:{train_data_path}")
    print(f"test_date_here:{test_data_path}")

    data_transformation=datacleaning()
    clean_training_df,clean_testing_df,_= data_transformation.clean_and_prepare_data(train_data_path,test_data_path)