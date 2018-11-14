from ..api.app import db

Exams = db.Table(
    'exams',
    db.Column(
        'student_name',
        db.Integer,
        db.ForeignKey('student.name'), primary_key=True),
    db.Column(
        'module_code',
        db.Integer,
        db.ForeignKey('module.code'), primary_key=True)
)
