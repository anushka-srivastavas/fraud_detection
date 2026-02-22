# Fraud Detection System

A Python-based credit card fraud detection project that uses machine learning to detect fraudulent transactions. The project includes data preprocessing, model training, evaluation, and deployment-ready components.

## Features

- Data preprocessing and feature engineering
- Train machine learning models for fraud detection
- Evaluate model performance with accuracy, precision, recall, and F1-score
- Modular project structure for easy extension and deployment

## Project Structure

```
fraud_detection/
├── data/            # Dataset (creditcard.csv or creditcard.zip)
├── notebooks/       # EDA and experiments
├── src/             # Python modules for preprocessing, training, and evaluation
├── models/          # Trained models and scalers
├── app/             # Deployment scripts or web app code
├── requirements.txt # Python dependencies
└── LICENSE          # MIT License
```

## Installation

1.Clone the repository:

```bash
git clone https://github.com/anushka-srivastavas/Fraud_detection.git
cd Fraud_detection

2.Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

3.Install dependencies:
pip install -r requirements.txt

Usage
1.	Place your dataset in the data/ folder. If using creditcard.csv, it may be zipped as creditcard.zip due to GitHub size limits.
2.	Run preprocessing, training, or evaluation scripts from the src/ folder:

python src/data_preprocessing.py
python src/train.py
python src/evaluate.py

Launch Deployment App
python app/main.py

Dataset

The project uses the Credit Card Fraud Detection dataset. For GitHub upload limits, the CSV is provided as a zip (creditcard.zip) in the data/ folder.

License

This project is licensed under the MIT License. See the LICENSE file for details.
