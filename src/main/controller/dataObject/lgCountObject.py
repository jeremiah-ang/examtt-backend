class LgCountObject:

    INDEX_LIFEGROUP = 0
    INDEX_COUNT = 1

    def __init__(self):
        self.obj = []

    def add_entries(self, entries):
        for entry in entries:
            self.add_entry(entry)

    def add_entry(self, entry):
        self.obj.append({
            "lifegroup": entry[self.INDEX_LIFEGROUP],
            "count": entry[self.INDEX_COUNT]
        })
