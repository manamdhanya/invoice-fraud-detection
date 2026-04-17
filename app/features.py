import re
from datetime import datetime

GST_REGEX = r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b"

def has_future_date(text):
    dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)
    for d in dates:
        try:
            if datetime.strptime(d, "%d-%m-%Y") > datetime.now():
                return 1
        except:
            continue
    return 0


def amount_anomaly(text):
    text = text.lower()
    numbers = list(map(int, re.findall(r"\d{3,}", text)))

    if len(numbers) < 3:
        return 0

    total = numbers[-1]
    items = numbers[:-1]

    if sum(items) > total:
        return 1

    return 0


def missing_fields(text):
    numbers = re.findall(r"\d{3,}", text)
    return 1 if len(numbers) < 3 else 0


def extract_features(text):
    return {
        "gstin_valid": 1 if re.search(GST_REGEX, text) else 0,
        "foreign_currency": 1 if any(c in text for c in ["$", "€", "BTC"]) else 0,
        "future_date": has_future_date(text),
        "suspicious_vendor": 1 if any(w in text.upper() for w in ["FAKE", "$$$", "XXXXX"]) else 0,
        "amount_anomaly": amount_anomaly(text),
        "missing_fields": missing_fields(text)
    }