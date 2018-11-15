from ..api.app import db


class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    time = db.Column(db.String(4))
    venue = db.Column(db.Integer, db.ForeignKey('venue.id'))
    modules = db.relationship('Module', backref='slot', lazy=True)
