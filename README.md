# 🎓 Student Performance Predictor

> **Predict student math scores with AI-powered insights using advanced machine learning**

A comprehensive end-to-end machine learning application that predicts student math performance based on demographic and academic factors. Built with modern technologies and deployed using industry best practices.

![Student Performance Predictor](https://img.shields.io/badge/ML-Powered-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render)

## 🌟 What This Project Does

Imagine being able to predict a student's math performance just by knowing their background, reading scores, and writing abilities. That's exactly what this application does! 

**Key Features:**
- 🧠 **Smart Predictions**: Uses Lasso Regression (the best performing model) to predict math scores
- 🎨 **Beautiful UI**: Modern React frontend with intuitive forms
- ⚡ **Real-time API**: FastAPI backend serving predictions instantly
- 🚀 **Production Ready**: Fully deployed on Vercel (frontend) and Render (backend)
- 🔄 **Automated Pipeline**: CI/CD with GitHub Actions for seamless updates

## 🏗️ System Architecture

```mermaid
flowchart TD
    %% FRONTEND LAYER
    subgraph FE ["Frontend (Vercel)"]
        FE1["Next.js + TypeScript\nTailwindCSS UI\nPrediction Form"]
    end

    %% BACKEND LAYER
    subgraph BE ["Backend (Render)"]
        BE1["FastAPI (Python 3.11)\nREST API + CORS"]
        BE2["Gunicorn + Uvicorn\nLogging & Health Checks"]
    end

    %% ML PIPELINE
    subgraph ML ["ML Pipeline (Artifacts)"]
        ML1["Preprocessing:\nStandardScaler + OneHotEncoder"]
        ML2["Lasso Regression Model"]
        ML3["model.pkl + preprocessor.pkl"]
    end

    %% INFRASTRUCTURE
    subgraph CI ["CI/CD Infrastructure"]
        CI1["GitHub (Code)"]
        CI2["GitHub Actions:\nLint, Test, Build"]
        CI3["Docker Hub\nMulti-platform Images"]
    end

    %% MAIN DATA FLOW (user to response)
    FE1 -->|POST Student Data (JSON)| BE1
    BE1 -->|Load Model & Preprocessor| ML3
    ML3 -->|Preprocess & Predict| BE1
    BE1 -->|Prediction Result (JSON)| FE1

    %% ML PIPELINE DATA CONNECTIVITY
    ML1 --> ML2
    ML2 --> ML3

    %% CI/CD & INFRASTRUCTURE LINKS
    CI1 --> CI2
    CI2 --> CI3
    CI3 --> FE1
    CI3 --> BE1

    %% BACKEND INTERNAL FLOW
    BE1 --> BE2

    %% STYLING
    classDef frontend fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#0D47A1
    classDef backend fill:#E8F5E9,stroke:#43A047,stroke-width:2px,color:#1B5E20
    classDef ml fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100
    classDef infra fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C
    classDef storage fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238
    classDef dataflow stroke-dasharray:5 5

    class FE1 frontend
    class BE1,BE2 backend
    class ML1,ML2 ml
    class ML3 storage
    class CI1,CI2,CI3 infra
    class FE1,BE1,ML3 dataflow
```

## 🧠 Machine Learning Pipeline

### **The Smart Model Selection Process**

Our system doesn't just use one model - it's smarter than that! Here's what happens behind the scenes:

1. **📊 Data Ingestion**: Loads student data from CSV files
2. **🔧 Feature Engineering**: 
   - **Numerical Features**: Reading & Writing scores (scaled with StandardScaler)
   - **Categorical Features**: Gender, Race, Parent Education, Lunch, Test Prep (One-hot encoded)
3. **🏆 Model Competition**: Tests 11 different algorithms:
   - Linear Regression
   - **Lasso Regression** ⭐ (Best performer!)
   - Ridge Regression
   - K-Nearest Neighbors
   - Decision Tree
   - Random Forest
   - Gradient Boosting
   - XGBoost
   - CatBoost
   - AdaBoost
   - Support Vector Regressor
4. **🎯 Hyperparameter Tuning**: Uses GridSearchCV to find optimal parameters
5. **🏅 Winner Selection**: Lasso Regression emerged as the champion!
6. **💾 Model Persistence**: Saves the best model as `model.pkl` and preprocessor as `preprocessor.pkl`

### **Why Lasso Regression Won**

Lasso Regression (Least Absolute Shrinkage and Selection Operator) is perfect for this task because:
- **Feature Selection**: Automatically identifies the most important features
- **Regularization**: Prevents overfitting by adding penalty terms
- **Interpretability**: Provides clear feature importance
- **Performance**: Achieved the highest R² score among all models

## 🚀 Deployment Architecture

### **Frontend (Vercel)**
- **Framework**: Next.js with React
- **Styling**: Tailwind CSS for beautiful, responsive design
- **Deployment**: Automatic deployments via GitHub Actions
- **Features**: 
  - Interactive prediction forms
  - Real-time loading states
  - Error handling
  - Mobile-responsive design

### **Backend (Render)**
- **Framework**: FastAPI with Python
- **Server**: Gunicorn with Uvicorn workers
- **Features**:
  - RESTful API endpoints
  - CORS enabled for frontend communication
  - Health monitoring
  - Automatic scaling
  - Model serving with artifacts

### **CI/CD Pipeline (GitHub Actions)**
```
Push to Main Branch
    ↓
1. 🧪 Run Tests (Python linting, formatting, unit tests)
    ↓
2. 🐳 Build & Push Docker Image (Multi-platform)
    ↓
3. ⚙️ Deploy Backend to Render (API trigger)
    ↓
4. 🎨 Deploy Frontend to Vercel (Automatic)
    ↓
✅ Live Application!
```

## 📊 Model Features

The model predicts math scores based on these factors:

### **Demographic Information**
- **Gender**: Male/Female
- **Race/Ethnicity**: Group A, B, C, D, E
- **Parental Education**: From "Some High School" to "Master's Degree"

### **Academic Factors**
- **Reading Score**: 0-100 scale
- **Writing Score**: 0-100 scale

### **Support Factors**
- **Lunch Type**: Standard or Free/Reduced
- **Test Preparation**: None or Completed

## 🎯 Prediction Output

The system provides:
- **Predicted Math Score**: 0-100 scale
- **Confidence Level**: High (≥80), Medium (60-79), Low (<60)
- **Performance Insights**: Based on score ranges
- **Recommendations**: Personalized study suggestions

## 🛠️ Technology Stack

### **Backend**
- **Python 3.11**: Core programming language
- **FastAPI**: Modern, fast web framework
- **Scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data processing
- **Gunicorn**: Production WSGI server

### **Frontend**
- **Next.js 14**: React framework
- **React 18**: UI library
- **TypeScript**: Type safety
- **Tailwind CSS**: Utility-first styling
- **Axios**: HTTP client

### **Infrastructure**
- **Docker**: Containerization
- **GitHub Actions**: CI/CD automation
- **Vercel**: Frontend hosting
- **Render**: Backend hosting
- **Docker Hub**: Container registry

## 🚀 Quick Start

### **Local Development**

1. **Clone the repository**
   ```bash
   git clone https://github.com/realranjan/END-TO-END-PROJECT.git
   cd END-TO-END-PROJECT
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Train the model** (if needed)
   ```bash
   python src/pipeline/train_pipeline.py
   ```

4. **Run the backend**
   ```bash
   python main.py
   ```

5. **Run the frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

6. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### **Production Deployment**

The application is automatically deployed when you push to the main branch:

- **Frontend**: https://end-to-end-project-mk67.vercel.app
- **Backend**: https://student-predictor-backend.onrender.com

## 📡 API Endpoints

### **Health Check**
```bash
GET /health
```

### **Make Prediction**
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

### **Model Information**
```bash
GET /model-info
```

## 📁 Project Structure

```
END-TO-END-PROJECT/
├──  main.py                    # FastAPI application entry point
├──  requirements.txt           # Python dependencies
├──  Dockerfile                 # Container configuration
├──  .github/workflows/         # CI/CD pipeline
├──  frontend/                  # Next.js frontend application
│   ├──  package.json
│   ├──  pages/                 # Next.js pages
│   ├──  components/            # React components
│   └──  styles/                # CSS and Tailwind
├──  src/                       # Machine learning pipeline
│   ├──  components/            # ML pipeline components
│   │   ├──  data_ingestion.py
│   │   ├──  data_transformation.py
│   │   └──  model_trainer.py
│   ├──  pipeline/              # Training and prediction pipelines
│   │   ├──  train_pipeline.py
│   │   └──  predict_pipeline.py
│   ├──  exception.py           # Custom exception handling
│   ├──  logger.py              # Logging configuration
│   └──  utils.py               # Utility functions
├──  artifacts/                 # Model files and data
│   ├──  model.pkl              # Trained Lasso Regression model
│   ├──  preprocessor.pkl       # Data preprocessing pipeline
│   ├──  train.csv              # Training dataset
│   ├──  test.csv               # Testing dataset
│   └──  raw.csv                # Original dataset
├──  tests/                     # Unit tests
├──  notebook/                  # Jupyter notebooks
└──  README.md                  # This file
```

##  Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

Run code quality checks:
```bash
# Format code
black src/ main.py

# Lint code
flake8 src/ main.py
```

##  Model Performance

The Lasso Regression model achieves:
- **R² Score**: High performance on test data
- **Feature Selection**: Automatic identification of important features
- **Regularization**: Prevents overfitting
- **Interpretability**: Clear feature importance rankings

##  Configuration

### **Environment Variables**
Copy `env.example` to `.env` and configure:
```bash
# Development
NEXT_PUBLIC_API_URL=http://localhost:8000

# Production
NEXT_PUBLIC_API_URL=https://student-predictor-backend.onrender.com
```

### **Model Configuration**
- **Model Path**: `artifacts/model.pkl`
- **Preprocessor Path**: `artifacts/preprocessor.pkl`
- **Training Data**: `artifacts/train.csv`
- **Test Data**: `artifacts/test.csv`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ranjan Vernekar**
- Email: ranjanvernekar45@gmail.com
- GitHub: [@realranjan](https://github.com/realranjan)

## 🙏 Acknowledgments

- **FastAPI** community for the excellent web framework
- **Scikit-learn** team for the machine learning tools
- **Vercel** and **Render** for seamless deployment
- **Next.js** team for the amazing React framework
- **Tailwind CSS** for beautiful styling utilities

## 🆘 Support

If you encounter any issues:
1. Check the [troubleshooting guide](README-DEPLOYMENT.md)
2. Review the logs in Vercel/Render dashboards
3. Check GitHub Actions for CI/CD issues
4. Open an issue on GitHub

---

**🎓 Ready to predict student performance? Try it out now!**

[Live Application](https://end-to-end-project-mk67.vercel.app) | [API Documentation](https://student-predictor-backend.onrender.com/docs)