from .dataObject import DataObject


class ExamttObject(DataObject):
    KEY_EXAMS = "exams"
    KEY_STUDENT = "students"
    KEY_MODULE = "modules"
    KEY_SLOT = "slots"
    KEY_VENUE = "venues"

    INDEX_EXAMS = 0
    INDEX_STUDENT = 1
    INDEX_MODULE = 2
    INDEX_SLOT = 3
    INDEX_VENUE = 4

    examtts = {
        KEY_EXAMS: [],
        KEY_STUDENT: {},
        KEY_MODULE: {},
        KEY_SLOT: {},
        KEY_VENUE: {}
    }

    def add_entries(self, entries):
        for entry in entries:
            self.add_entry(entry)
    
    def add_entry(self, entry):
        raise NotImplementedError
