from ..model.examtt import Examtt
from ..model.parser.myacesParser import MyacesParser
from ..model.parser.examttParser import ExamttParser


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
    
    def get_examtt_by_slot(slot_choice):
        return "hello"

    def page_not_found(self):
        return "Page Not Found!"
