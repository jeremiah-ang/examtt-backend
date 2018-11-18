from .examttObject import ExamttObject


class ExamttStudentObject(ExamttObject):
    def add_entry(self, entry):
        student = entry[self.INDEX_STUDENT]
        module = entry[self.INDEX_MODULE]
        slot = entry[self.INDEX_SLOT]
        venue = entry[self.INDEX_VENUE]
        self.add_student(student)
        student_obj = self.examtts[self.KEY_STUDENT][student.name]
        self.add_module(student_obj, module, slot, venue)

    def add_student(self, student):
        if student.name not in self.examtts[self.KEY_STUDENT]:
            self.examtts[self.KEY_STUDENT][student.name] = \
                {self.KEY_MODULE: []}

    def add_module(self, student_obj, module, slot, venue):
        student_obj[self.KEY_MODULE].append({
            "code": module.code,
            "time": slot.time,
            "day": slot.day,
            "venue": venue.name
        })
