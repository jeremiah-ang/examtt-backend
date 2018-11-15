from .examtt import Examtt


class Model:
    examtt = Examtt()

    def parse_and_add_entry(self, entry_str):
        self.examtt.parse_and_add_entry(entry_str)
