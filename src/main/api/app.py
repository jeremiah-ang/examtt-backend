import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
dbfile = os.path.join(project_dir, "..", "..", "database", "examtt.db")
DATABASE_URI = {
    "key": "SQLALCHEMY_DATABASE_URI",
    "filepath": "sqlite:///{}".format(dbfile)
}
app = Flask(__name__)
app.config[DATABASE_URI['key']] = DATABASE_URI['filepath']
db = SQLAlchemy(app)


from ..controller.controller import Controller
controller = Controller(db)


@app.route("/api/examtt", methods=['GET'])
def home():
    return controller.help()


@app.route(
    "/api/examtt/parse", methods=['POST'], defaults={'parser_choice': None})
@app.route("/api/examtt/parse/<parser_choice>", methods=['POST'])
def parse_examtt(parser_choice):
    examtt_str = request.get_json()['examtt']
    controller.parse_and_add_examtt_obj(examtt_str, parser_choice)
    return "Hello"


@app.route(
    "/api/examtt/slot", methods=['GET'], defaults={'slot_choice': None})
@app.route("/api/examtt/slot/<slot_choice>", methods=['GET'])
def get_examtt_by_slot(slot_choice):
    return controller.get_examtt_by_slot()


@app.errorhandler(404)
def page_not_found(err):
    return controller.page_not_found()


if __name__ == '__main__':
    app.run()
