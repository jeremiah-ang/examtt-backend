from ..api.app import db


class Slot(db.Model):
    id = db.Column(db.Integer, primay_key=True)
    day = db.Column(db.Integer)
    time = db.Column(db.String(4))
    modules = db.relationship('Module', backref='slot', lazy=True)
