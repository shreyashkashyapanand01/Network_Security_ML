# Network Security ML Project 🛡️

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![MLflow](https://img.shields.io/badge/MLflow-%23d9ead3.svg?style=flat&logo=numpy&logoColor=blue)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

An end-to-end machine learning pipeline for network security threat detection, specifically designed to identify phishing and malicious network activities. This production-ready system features automated data processing, model training with hyperparameter optimization, experiment tracking, and a web-based prediction service.

## 🚀 Features

### Core Capabilities
- **🔄 Automated Data Pipeline**: Seamless data ingestion from MongoDB with CSV export capabilities
- **✅ Data Validation**: Schema validation, data drift detection, and quality assurance
- **🔧 Data Transformation**: Advanced preprocessing with KNN imputation for missing values
- **🤖 Model Training**: Multiple classifier ensemble (Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost)
- **📊 Model Evaluation**: Comprehensive metrics tracking (F1-score, precision, recall)
- **🌐 Web API**: FastAPI-based prediction service with file upload support
- **📈 Experiment Tracking**: MLflow integration for model versioning and metrics logging
- **🐳 Containerization**: Docker support for seamless deployment
- **📝 Comprehensive Logging**: Detailed logging throughout the entire pipeline

### Technical Architecture
- **Modular Design**: Clean separation of concerns with distinct components
- **Configuration Management**: YAML-based schema and environment variable support
- **Production Ready**: Robust error handling and logging mechanisms
- **Scalable**: Designed for easy scaling and deployment

## 📁 Project Structure

```
Network_Security_ML/
├── networksecurity/           # Main package
│   ├── components/           # Core pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── entity/              # Configuration and artifact entities
│   ├── pipeline/            # Training and prediction pipelines
│   ├── utils/               # Utility functions and helpers
│   ├── exception/           # Custom exception handling
│   ├── logging/             # Logging configuration
│   └── constant/            # Constants and configurations
├── notebooks/               # Jupyter notebooks for analysis
├── data_schema/            # YAML schema definitions
├── Network_Data/           # Raw data storage
├── templates/              # HTML templates for web interface
├── final_model/            # Trained model artifacts
├── prediction_output/      # Prediction results
├── app.py                  # FastAPI web application
├── main.py                 # Training pipeline execution
├── push_data.py           # MongoDB data upload utility
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
└── setup.py              # Package installation setup
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10+
- MongoDB instance
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/shreyashkashyapanand01/Network_Security_ML.git
cd Network_Security_ML
```

### 2. Environment Setup
```bash
# Create virtual environment
conda create venv/

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
MONGODB_URL_KEY=your_mongodb_connection_string
MONGO_DB_URL=your_mongodb_connection_string
```

### 4. Install Package
```bash
pip install -e .
```

## 🚀 Usage

### Data Preparation
1. Place your raw CSV data in `Network_Data/phisingData.csv`
2. Upload data to MongoDB:
```bash
python push_data.py
```

### Training Pipeline
Execute the complete training pipeline:
```bash
python main.py
```

This will run:
- Data ingestion from MongoDB
- Data validation and quality checks
- Data transformation and preprocessing
- Model training with hyperparameter tuning
- Model evaluation and artifact generation

### Web Application
Start the FastAPI server:
```bash
python app.py
```

The application will be available at `http://localhost:8000`

#### API Endpoints:
- **GET /** - API documentation (Swagger UI)
- **GET /train** - Trigger model training pipeline
- **POST /predict** - Upload CSV file for batch predictions

### Docker Deployment
```bash
# Build Docker image
docker build -t network-security-ml .

# Run container
docker run -p 8000:8000 network-security-ml
```

## 🔧 Configuration

### Schema Configuration
Edit `data_schema/schema.yaml` to modify data validation rules and expected schema.

### Model Configuration
Modify hyperparameters and model selection in `networksecurity/components/model_trainer.py`.

## 📊 Model Performance

The system evaluates models using:
- **F1-Score**: Balanced measure of precision and recall
- **Precision**: Accuracy of positive predictions
- **Recall**: Coverage of actual positive cases

All experiments are tracked using MLflow for reproducibility and comparison.

## 🧪 Supported Models

- **Random Forest Classifier**
- **Decision Tree Classifier** 
- **Gradient Boosting Classifier**
- **Logistic Regression**
- **AdaBoost Classifier**

Each model undergoes hyperparameter optimization using GridSearchCV for optimal performance.

## 📝 Logging

Comprehensive logging is implemented throughout the pipeline:
- Pipeline execution logs in `logs/` directory
- MLflow experiment tracking for model metrics
- Error tracking and debugging information

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shreyash Kashyap**
- Email: shreyashkashyapanand@gmail.com
- GitHub: [@shreyashkashyapanand01](https://github.com/shreyashkashyapanand01)

## 🙏 Acknowledgments

- MongoDB for data storage capabilities
- FastAPI for the web framework
- MLflow for experiment tracking
- Scikit-learn for machine learning algorithms
- Docker for containerization support

---

⭐ If you find this project helpful, please consider giving it a star!