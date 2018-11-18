from ..model.examtt import Examtt
from .parser.myacesParser import MyacesParser
from .parser.examttParser import ExamttParser
from .dataObject.examttSlotObject import ExamttSlotObject
from .dataObject.examttStudentObject import ExamttStudentObject


class Controller:

    PARSER_CHOICE_MYACES = 'myaces'
    PARSER_CHOICES = [PARSER_CHOICE_MYACES]

    def __init__(self, db):
        self.examtt = Examtt(db)

    def help(self):
        return "Help Document"

    def parse_and_add_examtt_obj(self, examtt_obj, parser_choice):
        parser = ExamttParser()
        if parser_choice == self.PARSER_CHOICE_MYACES:
            parser = MyacesParser()
        self.examtt.add(parser.parse(examtt_obj))

    def get_examtt_by_slot(self, day, time, venue):
        examttBySlot = ExamttSlotObject()
        examttBySlot.add_entries(
            self.examtt.get_by_slot(day, time, venue))
        return examttBySlot.examtts

    def get_examtt_by_student(self, student_name):
        examttByStudent = ExamttStudentObject()
        examttByStudent.add_entries(
            self.examtt.get_by_student(student_name))
        return examttByStudent.examtts

    def page_not_found(self):
        return "Page Not Found!"
