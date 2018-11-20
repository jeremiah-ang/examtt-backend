from ..api.app import db


class Student(db.Model):

    name = db.Column(db.Text, primary_key=True)
    lifegroup = db.Column(
        db.Integer, db.ForeignKey('lifegroup.name'), nullable=False)
    exams = db.relationship(
        'Exams',
        backref='student',
        lazy=True)
