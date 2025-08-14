#!/bin/bash

# Student Performance Predictor Deployment Script
# This script automates the deployment process for the ML application

set -e

echo "🚀 Starting deployment process..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking deployment requirements..."
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    
    print_status "Requirements check passed!"
}

# Build and push Docker image
build_docker_image() {
    print_status "Building Docker image..."
    
    # Get current git commit hash for tagging
    GIT_COMMIT=$(git rev-parse --short HEAD)
    IMAGE_TAG="student-performance-predictor:${GIT_COMMIT}"
    
    docker build -t $IMAGE_TAG .
    
    if [ $? -eq 0 ]; then
        print_status "Docker image built successfully: $IMAGE_TAG"
    else
        print_error "Failed to build Docker image"
        exit 1
    fi
}

# Run tests
run_tests() {
    print_status "Running tests..."
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment..."
        python -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    pip install pytest pytest-cov
    
    # Run tests
    python -m pytest tests/ -v --cov=src
    
    if [ $? -eq 0 ]; then
        print_status "All tests passed!"
    else
        print_error "Tests failed. Deployment aborted."
        exit 1
    fi
    
    deactivate
}

# Deploy to local Docker
deploy_local() {
    print_status "Deploying to local Docker environment..."
    
    docker-compose down
    docker-compose up -d --build
    
    if [ $? -eq 0 ]; then
        print_status "Local deployment successful!"
        print_status "Application available at: http://localhost:8000"
    else
        print_error "Local deployment failed"
        exit 1
    fi
}

# Main deployment function
main() {
    print_status "Starting Student Performance Predictor deployment..."
    
    # Check requirements
    check_requirements
    
    # Run tests
    run_tests
    
    # Build Docker image
    build_docker_image
    
    # Deploy locally
    deploy_local
    
    print_status "🎉 Deployment completed successfully!"
    print_status "📊 Health check: http://localhost:8000/health"
    print_status "📚 API docs: http://localhost:8000/docs"
}

# Run main function
main "$@" 