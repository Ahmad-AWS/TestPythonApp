# app.py

from flask import Flask

app = Flask(__name__)

print ("Hello")
@app.route('/')
def hello():
    return 'Hello, this is a simple Python web app!'

