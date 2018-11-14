class Entry:
    def __init__(self, person, code, name, time, venue):
        self.person = person
        self.code = code
        self.name = name
        self.time = time
        self.venue = venue

    def __str__(self):
        return "%s: {[%s]%s || %s || %s}" % \
            (self.person, self.code, self.name, self.time, self.venue)
    
    def __eq__(self, other):
        if not isinstance(other, Entry): 
            return False
        return self.person == other.person and self.code == other.code and \
            self.name == other.name and self.time == other.time \
            and self.venue == other.venue
