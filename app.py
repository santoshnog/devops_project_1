from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
    return "Welcome to Linux"

@app.route("/phone")
def lwphone():
    return "+91-9740254232"