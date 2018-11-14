from flask import Flask
from controller import Controller

app = Flask(__name__)
controller = Controller()

@app.route("/", methods=['GET'])
def home():
    return controller.help()

@app.errorhandler(404)
def page_not_found():
    return controller.page_not_found()


if __name__ == '__main__':
    app.run()