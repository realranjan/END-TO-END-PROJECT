import sys
from dataclasses import dataclass
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn .preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


from src.exception import CustomException
from src.logger import logging
from src.utils import save_object



@dataclass
class Datacleaner:
    cleaning:str=os.path.join('artifacts','data_clean.pkl')

class datacleaning:
    def __init__(self):
        self.datacleaning=Datacleaner()

    def data_cleaning_build(self):

        try:
            numeric_columns=["writing_score","reading_score"]

            categorical_columns=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            numeric_cleaning_pipeline=Pipeline([
                ('filling_missing_values',SimpleImputer(strategy='median')),
                ('scale_numbers',StandardScaler())

            ])

            categorical_cleaning_pipeline=Pipeline([
                ('fill_missing_values',SimpleImputer(strategy='most_frequent')),
                ('encoding_of_text',OneHotEncoder()),
                ('convert_text_to_numbers',StandardScaler(with_mean=False))
                
            ])

            logging.info(f"numeric_columns_in cleaning{numeric_columns}")
            logging.info(f"categorical_columns_in cleaning{categorical_columns}")


            complete_data_cleaning_of_both=ColumnTransformer([
                ("clean_numbers",numeric_cleaning_pipeline,numeric_columns),
                ("clean_categorical_values",categorical_cleaning_pipeline,categorical_columns)
            ])
            
            return complete_data_cleaning_of_both

        except Exception as e:
            raise CustomException(e,sys)


    def clean_and_prepare_data(self,train_data_path,test_data_path):
        try:
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            logging.info("loading data files for cleaning and transformation")

            logging.info("undrgoing data cleaning ")
            data_cleaner=self.data_cleaning_build()

            target_column='math_score'

            x_train_df=train_data.drop(columns=[target_column],axis=1)
            y_train_df=train_data[target_column]

            x_test_df=test_data.drop(columns=[target_column],axis=1)
            y_test_df=test_data[target_column]

            logging.info("starting to clean test and train")

            clean_x_train_df=data_cleaner.fit_transform(x_train_df)
            clean_x_test_df=data_cleaner.transform(x_test_df)
 
            clean_training_df=np.c_[clean_x_train_df,np.array(y_train_df)]
            clean_testing_df=np.c_[clean_x_test_df,np.array(y_test_df)]

            logging.info("saving our data for future use")


            save_object(
                file_path=self.datacleaning.cleaning,obj=data_cleaner
            )


            return(
                clean_training_df,
                clean_testing_df,
                self.datacleaning.cleaning
            )
        except Exception as e:
            raise CustomException(e,sys)



