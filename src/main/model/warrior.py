from ..api.app import db


class Warrior(db.Model):
    name = db.Column(db.Text, primary_key=True)
