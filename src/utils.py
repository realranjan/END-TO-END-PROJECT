import pandas as pd
import numpy as np
import pickle
import dill
import os
import sys


from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
    try:

        folder_path=os.path.dirname(file_path)

        os.makedirs(folder_path,exist_ok=True)

        with open(file_path,'wb') as file_handle:
            dill.dump(obj,file_handle)

        print(f"saved object{file_path}")

    except Exception as e:
        CustomException(e,sys)



    
