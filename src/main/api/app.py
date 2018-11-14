from flask import Flask
from controller import Controller

app = Flask(__name__)
controller = Controller()

@app.route("/")
def home():
    return controller.help()