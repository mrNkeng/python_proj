# Financial Data Forecasting System

## Overview

The Financial Data Forecasting System is a sophisticated Python application designed to analyze and forecast financial data trends efficiently. Utilizing a Binary Search Tree (BST) for data management and a Flask API for easy data interaction, this system provides insightful and real-time financial data processing.

## Features

- **Efficient Data Management**: Implements a Binary Search Tree for efficient data sorting and retrieval, optimizing performance for large datasets.
- **Flask API**: A robust API built with Flask that facilitates the submission of financial data and returns processed results in real-time, enhancing system interactivity.
- **Containerization with Docker**: Ensures easy deployment and consistent operation across different computing environments using Docker.
- **Comprehensive Testing**: Includes a suite of unit tests that ensure all components perform as expected under various scenarios.

## How It Works

### Binary Search Tree (BST)

The application leverages a BST to manage financial data efficiently. Each node in the BST represents a financial data point (e.g., stock prices), allowing for operations like insertion, deletion, and retrieval in logarithmic time complexity. This structure enables quick access to sorted data, which is critical for timely financial analysis.

### Flask API

The system exposes a Flask-based API that accepts financial data via HTTP POST requests and uses the BST to process and sort this data. The sorted data can then be used for further statistical analysis or returned to the client as JSON.

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- Docker (optional for containerization)

### Setup

### Clone the repository to your local machine:

git clone https://github.com/yourusername/financial-data-forecasting.git
#cd financial-data-forecasting

### Create and activate a virtual environment (optional but recommended):
  - python -m venv venv
  - source venv/bin/activate  # On Unix/macOS
  - venv\Scripts\activate  # On Windows

### Install the required packages:
  - pip install -r requirements.txt

### Start the Flask application:
  - python app/main.py

### Docker Deployment
  Build the Docker image:
  - docker build -t financial-forecasting-app .

  Run the docker container
  - docker run -p 5001:5000 financial-forecasting-app

### Verifying Docker Deployment
After the container starts, use the same curl command to verify that the application is accessible and functioning correctly:
  - curl -X POST http://localhost:5001/forecast -H "Content-Type: application/json" -d '{"prices": [200, 100, 150, 300, 250]}'





