from ..api.app import db


class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(5))
    time = db.Column(db.String(4))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    warrior_name = db.Column(
        db.Text, db.ForeignKey('warrior.name'), nullable=True)
    modules = db.relationship('Module', backref='slot', lazy=True)
