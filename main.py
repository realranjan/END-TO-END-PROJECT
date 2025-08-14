from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
import numpy as np
import pandas as pd
import logging
import os
from typing import Dict, Any, Optional
import uvicorn

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StudentInput(BaseModel):
    gender: str = Field(..., description="Student gender (male/female)")
    race_ethnicity: str = Field(..., description="Race/ethnicity group (group A-E)")
    parental_level_of_education: str = Field(..., description="Parent education level")
    lunch: str = Field(..., description="Lunch type (standard/free/reduced)")
    test_preparation_course: str = Field(..., description="Test preparation status (none/completed)")
    reading_score: float = Field(..., ge=0, le=100, description="Reading score (0-100)")
    writing_score: float = Field(..., ge=0, le=100, description="Writing score (0-100)")

class PredictionResponse(BaseModel):
    predicted_math_score: float
    confidence_level: str
    input_data: Dict[str, Any]
    status: str

prediction_pipeline = PredictPipeline()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Student Performance Predictor API")
    try:
        logger.info("API startup completed successfully")
    except Exception as e:
        logger.error(f"Startup failed: {e}")
    
    yield
    
    logger.info("Shutting down Student Performance Predictor API")

app = FastAPI(
    title="Student Performance Predictor API",
    description="Predict student math scores based on demographic and academic factors using Machine Learning",
    version="2.0.0",
    lifespan=lifespan
)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Student Performance Predictor API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/health"
            }

@app.post("/api/predict", response_model=PredictionResponse)
async def predict_api(student_data: StudentInput):
    try:
        data = CustomData(
            gender=student_data.gender,
            race_ethnicity=student_data.race_ethnicity,
            parental_level_of_education=student_data.parental_level_of_education,
            lunch=student_data.lunch,
            test_preparation_course=student_data.test_preparation_course,
            reading_score=student_data.reading_score,
            writing_score=student_data.writing_score
        )
        
        pred_df = data.get_data_as_data_frame()
        results = prediction_pipeline.predict(pred_df)
        predicted_score = float(results[0])
        
        if predicted_score >= 80:
            confidence = "High"
        elif predicted_score >= 60:
            confidence = "Medium"
        else:
            confidence = "Low"
        
        logger.info(f"API prediction successful: {predicted_score}")
        
        return PredictionResponse(
            predicted_math_score=round(predicted_score, 2),
            confidence_level=confidence,
            input_data=student_data.dict(),
            status="success"
        )
        
    except Exception as e:
        logger.error(f"API prediction failed: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Prediction failed: {str(e)}"
        )

@app.get("/health")
async def health_check():
    try:
        test_pipeline = PredictPipeline()
        
        return {
            "status": "healthy", 
            "message": "Student Performance Predictor API is running",
            "version": "2.0.0",
            "endpoints": {
                "api_endpoint": "/api/predict",
                "documentation": "/docs",
                "health": "/health"
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }

@app.get("/model-info")
async def model_info():
    try:
        return {
            "model_files": {
                "trained_model": "artifacts/model.pkl",
                "preprocessor": "artifacts/preprocessor.pkl"
            },
            "supported_features": [
                "gender", "race_ethnicity", "parental_level_of_education",
                "lunch", "test_preparation_course", "reading_score", "writing_score"
            ],
            "output": "predicted_math_score",
            "score_range": "0-100",
            "model_type": "Regression",
            "status": "Model endpoints ready"
        }
    except Exception as e:
        return {"error": str(e), "status": "Model info unavailable"}

@app.get("/test")
async def test_endpoint():
    return {
        "message": "FastAPI test endpoint working",
        "timestamp": pd.Timestamp.now().isoformat(),
        "status": "success"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=False,  # Set to False for production
        log_level="info"
    )
