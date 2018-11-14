from ..api.app import db


class Module(db.Model):
    code = db.Column(db.String(20), primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeginKey('slot.id'), nullable=False)
    venue = db.Column(db.String(20), nullable=False)
