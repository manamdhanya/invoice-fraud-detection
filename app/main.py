from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.ocr import extract_text
from app.features import extract_features
from app.predict import predict
from app.graph import get_graph_flag

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")

@app.post("/predict")
async def predict_invoice(file: UploadFile = File(...)):

    content = await file.read()

    # OCR
    text = extract_text(content)
    print("\n=== OCR TEXT ===")
    print(text[:])

    # Features
    features = extract_features(text)
    '''print("\n=== FEATURES ===")
    for k, v in features.items():
        print(f"{k:20} : {v}")'''

    # ML + Graph
    ml_pred = predict(features)
    graph_pred = get_graph_flag(text)

    score = ml_pred * 2 + graph_pred
    final = 1 if score >= 2 else 0

    return {
        "prediction": "FRAUD" if final == 1 else "REAL",
        "features": features,
        "ocr_text": text[:],
        "graph_flag": graph_pred
    }