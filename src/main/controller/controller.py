from ..model.examtt import Examtt
from .parser.myacesParser import MyacesParser
from .parser.examttParser import ExamttParser
from .dataObject.examttSlotObject import ExamttSlotObject
from .dataObject.examttStudentObject import ExamttStudentObject
from .dataObject.examttCsv import ExamttCsv
from .dataObject.lgListObject import LgListObject
from .dataObject.lgCountObject import LgCountObject


class Controller:

    PARSER_CHOICE_MYACES = 'myaces'
    PARSER_CHOICES = [PARSER_CHOICE_MYACES]

    def __init__(self, db):
        self.examtt = Examtt(db)

    def help(self):
        return "Help Document"

    def parse_and_add_examtt_obj(self, examtt_obj, lifegroup, parser_choice):
        parser = ExamttParser()
        if parser_choice == self.PARSER_CHOICE_MYACES:
            parser = MyacesParser()
        student_name = self.examtt.add(parser.parse(examtt_obj), lifegroup)
        return self.get_examtt_by_student(student_name)

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

    def delete_examtt_by_student_name(self, student_name):
        try:
            self.examtt.delete_by_student_name(student_name)
            return "Successfully Deleted {}".format(student_name)
        except Exception:
            return "Failed to Delete with exception: {}".format(Exception)

    def get_examtt_as_csv(self):
        examttCsv = ExamttCsv()
        examttCsv.add_entries(self.examtt.get_by_slot(None, None, None))
        return examttCsv.get_csv()

    def get_all_lg(self):
        lgListObject = LgListObject()
        lgListObject.add_lgs(self.examtt.get_all_lg())
        return lgListObject.lgs

    def get_lg_count(self):
        lgCount = self.examtt.get_lg_count()
        lgCountObject = LgCountObject()
        lgCountObject.add_entries(lgCount)
        return lgCountObject.obj

    def page_not_found(self):
        return "Page Not Found!"
