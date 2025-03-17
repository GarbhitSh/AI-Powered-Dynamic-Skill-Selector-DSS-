# skills.py
import time
import random

def price_prediction():
    start = time.time()
    accuracy = random.uniform(0.7, 0.95)
    return {"price": round(random.uniform(50, 500), 2)}, {"accuracy": accuracy, "runtime": time.time() - start}

def data_fetcher():
    start = time.time()
    latency = random.uniform(0.1, 0.5)
    return {"data": "Fetched successfully"}, {"latency": latency, "runtime": time.time() - start}

def fraud_detection():
    start = time.time()
    fraud_score = random.uniform(0, 1)
    return {"fraud_score": fraud_score}, {"accuracy": 0.9, "runtime": time.time() - start}

SKILLS = {
    "price_prediction": price_prediction,
    "data_fetcher": data_fetcher,
    "fraud_detection": fraud_detection,
}
