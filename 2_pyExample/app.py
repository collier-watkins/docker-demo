# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World! This is a basic webpage served by a Dockerized Python app.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
