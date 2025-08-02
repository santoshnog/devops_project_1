from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
    return "Welcome to Linux"

@app.route("/phone")
def lwphone():
    return "+91-9740254232"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)