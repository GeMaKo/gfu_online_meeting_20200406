from app import app
import random
import datetime
import functions
import pandas as pd
from flask import request
from flask import jsonify
import joblib

MODEL = joblib.load("my_model.pkl")


@app.route("/", methods=["POST"])
def prediction():
    data_json = request.get_json(force=True)["data"]  # Get data posted as a json
    data = pd.read_json(data_json, orient='records')
    result = MODEL.predict(data)
    return jsonify(results=result.tolist())


@app.route("/health/check", methods=["GET"])
def health_check():
    return jsonify(
        {
            "status": "running",
            "version": "0.0.1",  # PLACEHOLDER
            "timestamp": datetime.datetime.now().strftime("%a, %d %b %Y %I:%M:%S %z"),
            "random": str(random.random() * 1000),
        }
    )