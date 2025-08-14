# 🚀 Student Performance Predictor - Deployment Guide

This guide covers the complete CI/CD pipeline setup and deployment to Vercel (Frontend), Render (Backend), and Docker (Model Serving).

## 📋 Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [CI/CD Pipeline Setup](#cicd-pipeline-setup)
3. [Frontend Deployment (Vercel)](#frontend-deployment-vercel)
4. [Backend Deployment (Render)](#backend-deployment-render)
5. [Docker Model Serving](#docker-model-serving)
6. [Environment Configuration](#environment-configuration)
7. [Monitoring & Health Checks](#monitoring--health-checks)
8. [Troubleshooting](#troubleshooting)

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   Docker       │
│   (Vercel)      │◄──►│   (Render)      │◄──►│   (Model)      │
│                 │    │                 │    │                 │
│ • Next.js       │    │ • FastAPI       │    │ • ML Pipeline  │
│ • React         │    │ • ML Models     │    │ • Preprocessor  │
│ • Tailwind CSS  │    │ • Data Pipeline │    │ • Artifacts     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔄 CI/CD Pipeline Setup

### Prerequisites

1. **GitHub Repository** with your code
2. **Docker Hub Account** for container registry
3. **Vercel Account** for frontend deployment
4. **Render Account** for backend deployment

### GitHub Secrets Setup

Add these secrets to your GitHub repository (`Settings > Secrets and variables > Actions`):

```bash
# Docker Hub
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-password

# Vercel
VERCEL_TOKEN=your-vercel-token
ORG_ID=your-vercel-org-id
PROJECT_ID=your-vercel-project-id

# Render
RENDER_SERVICE_ID=your-render-service-id
RENDER_API_KEY=your-render-api-key
```

### Pipeline Workflow

The CI/CD pipeline (`/.github/workflows/ci-cd.yml`) includes:

1. **Test Stage**: Run tests and linting
2. **Build Stage**: Build and push Docker image
3. **Deploy Backend**: Deploy to Render
4. **Deploy Frontend**: Deploy to Vercel

## 🌐 Frontend Deployment (Vercel)

### Setup Steps

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy Frontend**:
   ```bash
   cd frontend
   vercel --prod
   ```

4. **Configure Environment Variables**:
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add: `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com`

### Frontend Structure

```
frontend/
├── components/          # React components
├── pages/              # Next.js pages
├── styles/             # CSS and Tailwind
├── package.json        # Dependencies
├── next.config.js      # Next.js config
├── tailwind.config.js  # Tailwind config
└── vercel.json         # Vercel config
```

## ⚙️ Backend Deployment (Render)

### Setup Steps

1. **Connect GitHub Repository**:
   - Go to Render Dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**:
   ```
   Name: student-predictor-backend
   Environment: Python
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   ```

3. **Environment Variables**:
   ```
   PYTHON_VERSION=3.10.0
   PORT=8000
   ```

4. **Health Check Path**: `/health`

### Backend Configuration

The backend automatically detects Render environment and configures:
- Port binding to `$PORT`
- CORS for frontend communication
- Health check endpoints

## 🐳 Docker Model Serving

### Local Development

1. **Build Image**:
   ```bash
   docker build -t student-performance-predictor .
   ```

2. **Run Container**:
   ```bash
   docker run -p 8000:8000 student-performance-predictor
   ```

3. **Docker Compose**:
   ```bash
   docker-compose up -d
   ```

### Production Deployment

The Docker image serves as the model container and can be deployed to:
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **Kubernetes clusters**

## 🔧 Environment Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```bash
# Development
NEXT_PUBLIC_API_URL=http://localhost:8000

# Production
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
```

### Configuration Files

- **Frontend**: `frontend/.env.local`
- **Backend**: Environment variables in Render
- **Docker**: `Dockerfile` and `docker-compose.yml`

## 📊 Monitoring & Health Checks

### Health Check Endpoints

- **Backend Health**: `GET /health`
- **Model Info**: `GET /model-info`
- **API Status**: `GET /api/status`

### Monitoring Features

- **Logging**: Structured logging throughout the pipeline
- **Metrics**: Request/response monitoring
- **Error Tracking**: Custom exception handling
- **Performance**: Response time tracking

## 🚨 Troubleshooting

### Common Issues

1. **Frontend Can't Connect to Backend**:
   - Check `NEXT_PUBLIC_API_URL` in Vercel
   - Verify CORS configuration
   - Check backend health status

2. **Docker Build Fails**:
   - Verify Dockerfile syntax
   - Check requirements.txt dependencies
   - Ensure proper file permissions

3. **Render Deployment Issues**:
   - Check build logs in Render dashboard
   - Verify Python version compatibility
   - Check start command syntax

4. **CI/CD Pipeline Failures**:
   - Review GitHub Actions logs
   - Verify all secrets are configured
   - Check branch protection rules

### Debug Commands

```bash
# Check backend health
curl https://your-backend.onrender.com/health

# Test frontend API
curl -X POST https://your-frontend.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"gender":"male","race_ethnicity":"group A",...}'

# Docker logs
docker logs <container-id>

# Render logs
# Check in Render dashboard → Logs tab
```

## 📈 Performance Optimization

### Frontend
- **Code Splitting**: Next.js automatic code splitting
- **Image Optimization**: Next.js image optimization
- **Caching**: Vercel edge caching

### Backend
- **Async Processing**: FastAPI async endpoints
- **Connection Pooling**: Database connection optimization
- **Caching**: Response caching for predictions

### Docker
- **Multi-stage Builds**: Optimized image layers
- **Health Checks**: Container health monitoring
- **Resource Limits**: Memory and CPU constraints

## 🔒 Security Considerations

1. **Environment Variables**: Never commit secrets
2. **CORS Configuration**: Restrict to trusted domains
3. **Input Validation**: Validate all user inputs
4. **Rate Limiting**: Implement API rate limiting
5. **HTTPS**: Force HTTPS in production

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Render Documentation](https://render.com/docs)
- [Docker Documentation](https://docs.docker.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)

## 🤝 Support

For deployment issues:
1. Check the troubleshooting section above
2. Review logs in respective platforms
3. Check GitHub Actions for CI/CD issues
4. Verify environment variable configuration

---

**Happy Deploying! 🚀** 