from ..api.app import db


class Module(db.Model):
    code = db.Column(db.String(20), primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeignKey('slot.id'), nullable=False)
