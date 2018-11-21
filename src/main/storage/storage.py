from ..model.exams import Exams
from ..model.module import Module
from ..model.slot import Slot
from ..model.student import Student
from ..model.venue import Venue
from ..model.lifegroup import Lifegroup
from sqlalchemy import and_, func


class Storage:

    def __init__(self, db):
        self.db = db

    def exists_student(self, student):
        return self.db.session.query(self.db.exists().where(
            Student.name == student.name)).scalar()

    def exists_module(self, module):
        return self.db.session.query(self.db.exists().where(
            Module.code == module.code)).scalar()

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
        existing_student = Student.query.get(student.name)
        if existing_student is None:
            self.db.session.add(student)
        else:
            existing_student.lifegroup = student.lifegroup

    def add_or_update_module(self, module):
        existing_module = Module.query.get(module.code)
        if existing_module is None:
            self.db.session.add(module)
        else:
            existing_module.slot_id = module.slot_id

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
        self.add_slot(slot)
        return Slot.query.filter_by(
            day=slot.day,
            time=slot.time,
            venue_id=slot.venue_id).first_or_404().id

    def get_lifegroup(self, lifegroup_name):
        return Lifegroup.query.get(lifegroup_name)

    def get_examtt_by_slots_kwargs(self, day=None, time=None, venue=None):
        kwargs = {"slot": {}, "venue": {}}
        if day is not None:
            kwargs['slot']['day'] = day
        if time is not None:
            kwargs['slot']['time'] = time
        if venue is not None:
            kwargs['venue']['name'] = venue

        return self.get_examtt_by_kwargs(
            slot_args=kwargs['slot'], venue_args=kwargs['venue'])

    def get_examtt_by_kwargs(
            self,
            student_args={}, module_args={},
            slot_args={}, venue_args={}):
        return self.db.session.query(Exams, Student, Module, Slot, Venue)\
            .join(Student).filter_by(**student_args)\
            .join(Module).filter_by(**module_args)\
            .join(Slot).filter_by(**slot_args)\
            .join(Venue).filter_by(**venue_args)\
            .all()

    def get_examtt_by_student(self, student):
        return self.get_examtt_by_kwargs(student_args={"name": student})

    def delete_examtt_by_student_name(self, student_name):
        Student.query.filter_by(name=student_name).delete()
        Exams.query.filter_by(student_name=student_name).delete()

    def delete_exams(self, student=None, module=None):
        kwargs = {}
        if student is not None:
            kwargs["student_name"] = student.name
        if module is not None:
            kwargs["module_code"] = module.code
        return Exams.query.filter_by(**kwargs).delete()

    def get_all_lg(self):
        return Lifegroup.query.all()

    def get_lg_count(self):
        return self.db.session.query(
            Student.lifegroup, func.count(Student.lifegroup))\
            .group_by(Student.lifegroup).all()

    def commit(self):
        self.db.session.commit()
