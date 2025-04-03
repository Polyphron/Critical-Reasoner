from flask import Flask, jsonify
import requests

app = Flask(__name__)

RAW_URL = "https://raw.githubusercontent.com/Polyphron/Critical-Reasoner/main/Critical%20Reasoner%20v2.0.txt"

@app.route("/")
def home():
    return "Critical Reasoner API is running!"

@app.route("/reasoner-rules", methods=["GET"])
def get_reasoner_rules():
    try:
        response = requests.get(RAW_URL)
        response.raise_for_status()
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
