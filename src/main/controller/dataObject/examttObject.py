from .dataObject import DataObject


class ExamttObject(DataObject):
    KEY_EXAMS = "exams"
    KEY_STUDENT = "students"
    KEY_MODULE = "modules"
    KEY_SLOT = "slots"
    KEY_VENUE = "venues"
    KEY_LIFEGROUP = "lifegroup"

    INDEX_EXAMS = 0
    INDEX_STUDENT = 1
    INDEX_MODULE = 2
    INDEX_SLOT = 3
    INDEX_VENUE = 4

    def __init__(self):
        self.examtts = {
            self.KEY_EXAMS: [],
            self.KEY_STUDENT: {},
            self.KEY_MODULE: {},
            self.KEY_SLOT: {},
            self.KEY_VENUE: {}
        }

    def add_entries(self, entries):
        for entry in entries:
            self.add_entry(entry)
    
    def add_entry(self, entry):
        raise NotImplementedError
