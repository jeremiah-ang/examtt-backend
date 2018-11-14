from ..storage.storage import Storage
from .entry import Entry

class Examtt:
    def __init__(self):
        self.storage = Storage()

    def parse_and_add_entry(self, entry_str):
        self.add(self.parse(entry_str))
    
    def add(self, entry):
        self.storage.add(entry)
        pass
    
    def parse(self, entry_str):
        return Entry("Jeremiah", "CS4234", "Optimisation Algorithm", "1300", "MPSH")
