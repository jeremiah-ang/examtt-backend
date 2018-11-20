from ..api.app import db


class Lifegroup(db.Model):
    name = db.Column(db.Text, primary_key=True)
