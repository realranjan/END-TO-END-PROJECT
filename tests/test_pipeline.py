import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
from pipeline.train_pipeline import TrainPipeline

class TestDataIngestion:
    def test_data_ingestion_config(self):
        ingestion = DataIngestion()
        assert hasattr(ingestion.ingestion_config, 'train_data_path')
        assert hasattr(ingestion.ingestion_config, 'test_data_path')
        assert hasattr(ingestion.ingestion_config, 'raw_data_path')

class TestDataTransformation:
    def test_data_transformation_config(self):
        transformation = DataTransformation()
        assert hasattr(transformation.data_transformation_config, 'preprocessor_obj_file_path')
    
    def test_get_data_transformer_object(self):
        transformation = DataTransformation()
        preprocessor = transformation.get_data_transformer_object()
        assert preprocessor is not None

class TestModelTrainer:
    def test_model_trainer_config(self):
        trainer = ModelTrainer()
        assert hasattr(trainer.model_trainer_config, 'trained_model_file_path')

class TestTrainPipeline:
    def test_train_pipeline_initialization(self):
        pipeline = TrainPipeline()
        assert hasattr(pipeline, 'data_ingestion')
        assert hasattr(pipeline, 'data_transformation')
        assert hasattr(pipeline, 'model_trainer')

if __name__ == "__main__":
    pytest.main([__file__]) 