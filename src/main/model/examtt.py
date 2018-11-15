from ..storage.storage import Storage


class Examtt:
    def __init__(self):
        self.storage = Storage()

    def parse_and_add_exam(self, exams_str):
        self.add(self.parse(exams_str))

    def add(self, exam):
        pass

    def parse(self, exams_str):
        pass
