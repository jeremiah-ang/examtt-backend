from ..api.app import db


class Exams(db.Model):
    student_name = db.Column(
        db.Text,
        db.ForeignKey('student.name'),
        primary_key=True)
    module_code = db.Column(
        db.String(20),
        db.ForeignKey('module.code'),
        primary_key=True)
