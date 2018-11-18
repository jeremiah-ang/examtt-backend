from ..model.exams import Exams
from ..model.module import Module
from ..model.slot import Slot
from ..model.student import Student
from ..model.venue import Venue
from sqlalchemy import and_


class Storage:

    def __init__(self, db):
        self.db = db

    def exists_student(self, student):
        return self.db.session.query(self.db.exists().where(
            Student.name == student.name)).scalar()

    def exists_module(self, module):
        return self.db.session.query(self.db.exists().where(
            Module.code == module.code
            and Module.slot_id == module.slot_id)).scalar()

    def exists_venue(self, venue):
        return self.db.session.query(self.db.exists().where(
            Venue.name == venue.name)).scalar()

    def exists_slot(self, slot):
        return self.db.session.query(self.db.exists().where(and_(
            Slot.day == slot.day,
            Slot.time == slot.time,
            Slot.venue_id == slot.venue_id))).scalar()

    def exists_exams(self, exams):
        return self.db.session.query(self.db.exists().where(and_(
            Exams.student_name == exams.student_name,
            Exams.module_code == exams.module_code))).scalar()

    def add_student(self, student):
        if not self.exists_student(student):
            self.db.session.add(student)

    def add_module(self, module):
        if not self.exists_module(module):
            self.db.session.add(module)

    def add_venue(self, venue):
        if not self.exists_venue(venue):
            self.db.session.add(venue)

    def add_slot(self, slot):
        if not self.exists_slot(slot):
            self.db.session.add(slot)

    def add_exams(self, exams):
        if not self.exists_exams(exams):
            self.db.session.add(exams)

    def get_venue_id(self, venue):
        self.add_venue(venue)
        return Venue.query.filter_by(name=venue.name).first_or_404().id

    def get_slot_id(self, slot):
        print(slot.day, slot.time, slot.venue_id)
        self.add_slot(slot)
        return Slot.query.filter_by(
            day=slot.day,
            time=slot.time,
            venue_id=slot.venue_id).first_or_404().id

    def commit(self):
        self.db.session.commit()
