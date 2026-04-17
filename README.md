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
│   ├── main.py          # FastAPI entry point
│   ├── predict.py       # Prediction logic
│   ├── features.py      # Feature extraction
│   ├── graph.py         # Graph-based detection
│   ├── ocr.py           # OCR processing
│
├── model/
│   ├── fraud_model.pkl
│   └── features.pkl
│
├── static/
│   └── index.html       # Frontend UI
│
├── requirements.txt
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

## Deployment

This project is configured for deployment using **Render** via `render.yaml`.

---

## Tech Stack

* **Frontend**: HTML, CSS, JavaScript (Canvas API)
* **Backend**: FastAPI
* **ML Model**: Scikit-learn
* **OCR**: Tesseract / custom pipeline

---

## Key Highlights

* Combines **rule-based + ML + graph detection**
* Interactive **visual UI (network graph background)**
* Modular backend design (clean separation of logic)

---

## Future Improvements

* Advanced ML models (deep learning / NLP)
* Graph database (Neo4j)
* Dashboard analytics
* User authentication


