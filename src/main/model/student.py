from ..api.app import db
from .exams import Exams


class Student(db.Model):

    name = db.Column(db.Text, primary_key=True)
    exams = db.relationship(
        'exams',
        secondary=Exams,
        lazy='subquery',
        backref=db.backref('Student', lazy=True))
