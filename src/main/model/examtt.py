from ..storage.storage import Storage
from .slot import Slot
from .module import Module
from .student import Student
from .venue import Venue
from .exams import Exams
from ..exceptions.noStudentNameException import NoStudentNameException
from ..exceptions.invalidLifegroupException import InvalidLifegroupException


class Examtt:

    def __init__(self, db):
        self.storage = Storage(db)

    def add(self, parser_result, lifegroup_str):
        if parser_result.student_name is None:
            raise NoStudentNameException

        lifegroup = self.storage.get_lifegroup(lifegroup_str)
        if lifegroup is None:
            raise InvalidLifegroupException
        student = Student(
            name=parser_result.student_name, lifegroup=lifegroup.name)
        self.storage.delete_exams(student=student)
        self.storage.add_student(student)
        for entry in parser_result.entries:
            venue = Venue(name=entry.venue)
            venue_id = self.storage.get_venue_id(venue)
            slot = Slot(day=entry.date, time=entry.time, venue_id=venue_id)
            slot_id = self.storage.get_slot_id(slot)
            module = Module(code=entry.module_code, slot_id=slot_id)
            self.storage.add_or_update_module(module)
            exam = Exams(student_name=student.name, module_code=module.code)
            self.storage.add_exams(exam)
        self.storage.commit()
        return student.name

    def get_by_slot(self, day, time, venue):
        return self.get_slots(day, time, venue)

    def get_slots(self, day, time, venue):
        return self.storage.get_examtt_by_slots_kwargs(day, time, venue)

    def get_by_student(self, student):
        return self.storage.get_examtt_by_student(student)

    def delete_by_student_name(self, student_name):
        self.storage.delete_examtt_by_student_name(student_name)
        self.storage.commit()
