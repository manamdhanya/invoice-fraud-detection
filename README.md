# Invoice Fraud Detection System

A full-stack application that detects fraudulent invoices using OCR, feature engineering, and graph-based anomaly analysis — with an interactive animated UI.

---

## Features

* Extracts text from invoices using OCR
* Validates invoice features (GSTIN, amount anomalies, etc.)
* Detects suspicious patterns using graph logic
* Animated frontend with network visualization
* Real-time fraud prediction API

---

## Project Structure

```
invoice-fraud-detection/
│
├── app/
│   ├── main.py
│   ├── predict.py
│   ├── features.py
│   ├── graph.py
│   ├── ocr.py
│
├── model/
│   ├── fraud_model.pkl
│   └── features.pkl
│
├── static/
│   └── index.html
│
├── requirements.txt
├── Dockerfile        
├── render.yaml
└── README.md
```

---

## How It Works

1. User uploads invoice
2. OCR extracts text
3. Features are generated
4. ML model predicts fraud
5. Graph logic checks suspicious relationships
6. Results displayed with UI visualization

---

## Running Locally

### 1. Clone repo

```
git clone https://github.com/YOUR_USERNAME/invoice-fraud-detection.git
cd invoice-fraud-detection
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run server

```
uvicorn app.main:app --reload
```

### 4. Open in browser

```
http://127.0.0.1:8000
```

---

## Running with Docker (Recommended)

This project uses Docker to enable full OCR support (Tesseract + Poppler).

### 1. Build Docker image

```
docker build -t invoice-fraud-app .
```

### 2. Run container

```
docker run -p 10000:10000 invoice-fraud-app
```

### 3. Open in browser

```
http://localhost:10000
```

---

## Deployment (Render + Docker)

1. Push code to GitHub
2. Go to Render Dashboard
3. Create **New Web Service**
4. Select your repo
5. Choose **Environment → Docker**
6. Deploy

---

## Tech Stack

* **Frontend**: HTML, CSS, JavaScript (Canvas API)
* **Backend**: FastAPI
* **ML Model**: Scikit-learn
* **OCR**: Tesseract + Poppler (via Docker)

---

## Key Highlights

* Combines **rule-based + ML + graph detection**
* Interactive **visual UI (network graph background)**
* Full OCR support (PDF + Image) using Docker
* Clean modular backend architecture

---

## Future Improvements

* Advanced ML models (deep learning / NLP)
* Graph database (Neo4j)
* Dashboard analytics
* User authentication

