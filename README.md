# Student Performance Predictor

An end-to-end machine learning project that predicts student math scores based on demographic and academic factors using FastAPI and modern ML techniques.

## Features

- **Machine Learning Model**: Regression model to predict student math scores
- **Web Interface**: User-friendly HTML forms for predictions
- **REST API**: Programmatic access via JSON endpoints
- **Real-time Predictions**: Instant score predictions with confidence levels
- **Model Monitoring**: Health checks and model information endpoints

## Model Features

The model predicts math scores based on:
- **Demographic Factors**: Gender, Race/Ethnicity
- **Educational Background**: Parental education level
- **Academic Factors**: Reading score, Writing score
- **Support Factors**: Lunch type, Test preparation course completion

## System Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │    │   API Client    │    │   Mobile App    │
│   (Browser)     │    │   (Python/JS)   │    │   (React Native)│
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │     FastAPI Server        │
                    │   (main.py)               │
                    │  ┌─────────────────────┐  │
                    │  │   Request Router    │  │
                    │  │   (URL Dispatching) │  │
                    │  └─────────┬───────────┘  │
                    │            │              │
                    │  ┌─────────▼───────────┐  │
                    │  │   Request Handler   │  │
                    │  │  (Form/API Logic)   │  │
                    │  └─────────┬───────────┘  │
                    └────────────┼──────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │   Prediction Pipeline     │
                    │  (predict_pipeline.py)    │
                    │  ┌─────────────────────┐  │
                    │  │   Data Validation   │  │
                    │  │   (CustomData)      │  │
                    │  └─────────┬───────────┘  │
                    │            │              │
                    │  ┌─────────▼───────────┐  │
                    │  │   Model Loading     │  │
                    │  │   (artifacts/)      │  │
                    │  └─────────┬───────────┘  │
                    │            │              │
                    │  ┌─────────▼───────────┐  │
                    │  │   Prediction        │  │
                    │  │   (ML Model)        │  │
                    │  └─────────────────────┘  │
                    └───────────────────────────┘
```

### Data Flow Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Raw Data      │    │   Data          │    │   Feature       │
│   (CSV Files)   │───▶│   Ingestion     │───▶│   Engineering   │
│                 │    │   Component     │    │   Component     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
┌─────────────────┐    ┌─────────────────┐    ┌───────▼───────┐
│   Model         │    │   Model         │    │   Data        │
│   Training      │◀───│   Evaluation    │◀───│   Splitting   │
│   Component     │    │   Component     │    │   (Train/Test)│
└─────────────────┘    └─────────────────┘    └───────────────┘
         │
         ▼
┌─────────────────┐
│   Model         │
│   Artifacts     │
│   (model.pkl)   │
└─────────────────┘
```

### Component Architecture

```
src/
├── components/                    # Core ML Components
│   ├── data_ingestion.py         # Data loading and splitting
│   ├── data_transformation.py    # Feature engineering & preprocessing
│   └── model_trainer.py          # Model training & evaluation
│
├── pipeline/                      # Pipeline Orchestration
│   ├── train_pipeline.py         # Training workflow
│   └── predict_pipeline.py       # Prediction workflow
│
├── utils.py                      # Utility functions
├── exception.py                  # Custom exception handling
└── logger.py                     # Logging configuration
```

### API Architecture

```
FastAPI Application (main.py)
├── Web Routes
│   ├── GET /                     # Landing page
│   ├── GET /predictdata          # Prediction form
│   └── POST /predictdata         # Form-based prediction
│
├── API Routes
│   ├── POST /api/predict         # JSON prediction endpoint
│   ├── GET /health               # Health check
│   ├── GET /model-info           # Model information
│   └── GET /test                 # Test endpoint
│
└── Error Handling
    ├── 404 Handler               # Custom 404 page
    └── Exception Handler         # Global error handling
```

### Model Architecture

```
Machine Learning Pipeline
├── Data Preprocessing
│   ├── Categorical Encoding      # One-hot encoding
│   ├── Feature Scaling          # StandardScaler
│   └── Missing Value Handling   # Imputation
│
├── Model Selection
│   ├── Linear Models            # LinearRegression, Ridge, Lasso
│   ├── Tree-based Models        # RandomForest, DecisionTree
│   ├── Ensemble Methods         # XGBoost, CatBoost, AdaBoost
│   └── Other Models             # SVR, KNN
│
├── Hyperparameter Tuning
│   ├── GridSearchCV             # Exhaustive search
│   └── Cross-validation         # 3-fold CV
│
└── Model Persistence
    ├── Model Serialization      # Pickle format
    └── Preprocessor Storage     # Pipeline artifacts
```

### Deployment Architecture

```
Production Deployment
├── Web Server (Uvicorn)
│   ├── Process Management       # Multiple workers
│   ├── Load Balancing           # Round-robin
│   └── Health Monitoring        # Health checks
│
├── Static File Serving
│   ├── CSS/JS Assets           # Static files
│   └── Template Rendering      # Jinja2 templates
│
├── Model Serving
│   ├── Model Loading           # On-demand loading
│   ├── Caching                 # Model caching
│   └── Version Management      # Model versioning
│
└── Monitoring & Logging
    ├── Application Logs        # Structured logging
    ├── Performance Metrics     # Response times
    └── Error Tracking          # Exception monitoring
```

## Technology Stack

- **Backend**: FastAPI, Python 3.8+
- **Machine Learning**: Scikit-learn, CatBoost, XGBoost
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, Jinja2 Templates
- **Deployment**: Uvicorn

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd END-TO-END-PROJECT
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Usage

### Web Interface
1. Open your browser and go to `http://localhost:8000`
2. Click on "Predict Data" to access the prediction form
3. Fill in the student information
4. Submit to get the predicted math score

### API Endpoints

#### Health Check
```bash
GET /health
```

#### Model Information
```bash
GET /model-info
```

#### Make Prediction (API)
```bash
POST /api/predict
Content-Type: application/json

{
    "gender": "female",
    "race_ethnicity": "group C",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "reading_score": 85.0,
    "writing_score": 88.0
}
```

#### Form-based Prediction
```bash
POST /predictdata
Content-Type: application/x-www-form-urlencoded
```

## Project Structure

```
END-TO-END-PROJECT/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── setup.py               # Package configuration
├── src/
│   ├── components/        # ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/          # Training and prediction pipelines
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py       # Custom exception handling
│   ├── logger.py          # Logging configuration
│   └── utils.py           # Utility functions
├── templates/             # HTML templates
│   ├── index.html
│   └── home.html
├── static/                # Static files (CSS, JS)
├── artifacts/             # Trained models and data
└── logs/                  # Application logs
```

## Development

### Training the Model
```bash
python src/pipeline/train_pipeline.py
```

### Running Tests
```bash
python -m pytest tests/
```

### Code Quality
```bash
# Install development dependencies
pip install black flake8 mypy

# Format code
black src/ main.py

# Lint code
flake8 src/ main.py

# Type checking
mypy src/ main.py
```

## Model Performance

The model uses ensemble methods (CatBoost, XGBoost) with hyperparameter tuning to achieve optimal performance. Model metrics are logged during training and can be monitored via the `/model-info` endpoint.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Ranjan Vernekar**
- Email: ranjanvernekar45@gmail.com

## Acknowledgments

- FastAPI community for the excellent web framework
- Scikit-learn team for the machine learning tools
- CatBoost and XGBoost teams for the ensemble methods