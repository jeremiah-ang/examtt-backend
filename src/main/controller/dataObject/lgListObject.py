class LgListObject:
    def __init__(self):
        self.lgs = []

    def add_lgs(self, lgs):
        self.lgs = [lg.name for lg in lgs]
