import pickle
import numpy as np

model = pickle.load(open("model/fraud_model.pkl", "rb"))
feature_order = pickle.load(open("model/features.pkl", "rb"))

def predict(features_dict):
    
    # Ensure correct order
    features = [features_dict[f] for f in feature_order]
    
    features = np.array(features).reshape(1, -1)
    
    return model.predict(features)[0]