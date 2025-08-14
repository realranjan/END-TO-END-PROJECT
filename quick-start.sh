#!/bin/bash

# Quick Start Script for Student Performance Predictor
# This script helps you get started quickly with the application

echo "🚀 Welcome to Student Performance Predictor!"
echo "=============================================="

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_step() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

# Check if Docker is running
check_docker() {
    print_step "Checking Docker status..."
    if ! docker info > /dev/null 2>&1; then
        echo "❌ Docker is not running. Please start Docker Desktop and try again."
        exit 1
    fi
    print_success "Docker is running!"
}

# Build and start the application
start_app() {
    print_step "Building and starting the application..."
    
    # Build Docker image
    docker build -t student-performance-predictor .
    if [ $? -ne 0 ]; then
        echo "❌ Failed to build Docker image"
        exit 1
    fi
    
    # Start with Docker Compose
    docker-compose up -d
    
    if [ $? -eq 0 ]; then
        print_success "Application started successfully!"
    else
        echo "❌ Failed to start application"
        exit 1
    fi
}

# Wait for application to be ready
wait_for_app() {
    print_step "Waiting for application to be ready..."
    
    max_attempts=30
    attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        if curl -s http://localhost:8000/health > /dev/null; then
            print_success "Application is ready!"
            break
        fi
        
        echo "⏳ Waiting for application... (attempt $attempt/$max_attempts)"
        sleep 2
        attempt=$((attempt + 1))
    done
    
    if [ $attempt -gt $max_attempts ]; then
        echo "❌ Application failed to start within expected time"
        exit 1
    fi
}

# Show application information
show_info() {
    echo ""
    echo "🎉 Application is running!"
    echo "=========================="
    echo "🌐 Frontend: http://localhost:8000"
    echo "📚 API Docs: http://localhost:8000/docs"
    echo "🏥 Health Check: http://localhost:8000/health"
    echo "📊 Model Info: http://localhost:8000/model-info"
    echo ""
    echo "💡 To stop the application, run: docker-compose down"
    echo "💡 To view logs, run: docker-compose logs -f"
    echo ""
}

# Main execution
main() {
    echo "Starting Student Performance Predictor..."
    echo ""
    
    check_docker
    start_app
    wait_for_app
    show_info
}

# Run main function
main "$@" 