# app/app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps!"

@app.route("/metrics")
def metrics():
    return "my_custom_metric 1\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

