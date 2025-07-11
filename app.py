from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()

import requests

app = Flask(__name__)
CORS(app)  # ✅ This now comes after app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}

def summarize_text(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.json.get('text', '')
    summary = summarize_text(input_text)
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)