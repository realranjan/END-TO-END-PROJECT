#!/usr/bin/env python3

import sys
import os
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

def test_prediction():
    try:
        print("Testing Prediction Pipeline...")
        
        sample_data = CustomData(
            gender="female",
            race_ethnicity="group C",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=85,
            writing_score=88
        )
        
        print("Sample data created successfully")
        
        df = sample_data.get_data_as_data_frame()
        print(f"DataFrame created with shape: {df.shape}")
        print(f"Sample data:\n{df.head()}")
        
        pipeline = PredictPipeline()
        print("Prediction pipeline initialized")
        
        prediction = pipeline.predict(df)
        print(f"Prediction result: {prediction[0]:.2f}")
        
        print("All tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False

def test_model_files():
    print("\nChecking model files...")
    
    model_path = os.path.join("artifacts", "model.pkl")
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
    
    if os.path.exists(model_path):
        print(f"Model file found: {model_path}")
    else:
        print(f"Model file missing: {model_path}")
        return False
    
    if os.path.exists(preprocessor_path):
        print(f"Preprocessor file found: {preprocessor_path}")
    else:
        print(f"Preprocessor file missing: {preprocessor_path}")
        return False
    
    return True

if __name__ == "__main__":
    print("Starting Student Performance Predictor Tests\n")
    
    model_files_ok = test_model_files()
    
    if model_files_ok:
        prediction_ok = test_prediction()
        
        if prediction_ok:
            print("\nAll tests completed successfully!")
            print("The application is ready to use.")
        else:
            print("\nPrediction test failed.")
            sys.exit(1)
    else:
        print("\nModel files test failed.")
        print("Please ensure the model has been trained.")
        sys.exit(1) 