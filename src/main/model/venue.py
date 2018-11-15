from ..api.app import db


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
