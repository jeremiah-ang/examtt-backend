from ..api.app import db


class Student(db.Model):

    name = db.Column(db.Text, primary_key=True)
    exams = db.relationship(
        'Exams',
        backref='student',
        lazy=True)
