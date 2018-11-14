import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from ..controller.controller import Controller

project_dir = os.path.dirname(os.path.abspath(__file__))
dbfile = os.path.join(project_dir, "..", "..", "database", "examtt.db")
DATABASE_URI = {
    "key": "SQLALCHEMY_DATABASE_URI",
    "filepath": "sqlite:///{}".format(dbfile)
}
app = Flask(__name__)
app.config[DATABASE_URI['key']] = DATABASE_URI['filepath']
db = SQLAlchemy(app)
controller = Controller()


@app.route("/", methods=['GET'])
def home():
    return controller.help()


@app.route("/parse", methods=['POST'])
def parse_examtt():
    print(request.get_json()['examtt'])
    return "Hello"


@app.errorhandler(404)
def page_not_found():
    return controller.page_not_found()


if __name__ == '__main__':
    app.run()
