class ParserResult:
    def __init__(self, student_name):
        self.student_name = student_name
        self.entries = []

    def add_entry(self, module_code, venue, date, time):
        self.entries.append(ParserResultEntry(module_code, venue, date, time))

    def __str__(self):
        return "Name: {}, Number of exams: {}".format(
            self.student_name, len(self.entries))


class ParserResultEntry:
    def __init__(self, module_code, venue, date, time):
        self.module_code = module_code
        self.venue = venue
        self.date = date
        self.time = time
