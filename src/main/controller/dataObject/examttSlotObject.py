from .examttObject import ExamttObject


class ExamttSlotObject(ExamttObject):
    def add_entry(self, entry):
        slot = entry[self.INDEX_SLOT]
        venue = entry[self.INDEX_VENUE]
        module = entry[self.INDEX_MODULE]
        student = entry[self.INDEX_STUDENT]
        self.add_slot(slot, venue)
        slot_venue_obj = \
            self.examtts[self.KEY_SLOT][slot.id][self.KEY_VENUE][venue.id]
        venue_slot_obj = \
            self.examtts[self.KEY_VENUE][venue.id][self.KEY_SLOT][slot.id]
        self.add_module(slot_venue_obj, venue_slot_obj, module, student)
    
    def add_slot(self, slot, venue):
        if slot.id not in self.examtts[self.KEY_SLOT]:
            self.examtts[self.KEY_SLOT][slot.id] = {
                "day": slot.day,
                "time": slot.time,
                self.KEY_VENUE: {}
            }
        if venue.id not in \
                self.examtts[self.KEY_SLOT][slot.id][self.KEY_VENUE]:
            self.examtts[self.KEY_SLOT][slot.id][self.KEY_VENUE][venue.id] = {}

        if venue.id not in self.examtts[self.KEY_VENUE]:
            self.examtts[self.KEY_VENUE][venue.id] = {
                "name": venue.name,
                self.KEY_SLOT: {}
            }

        if slot.id not in \
                self.examtts[self.KEY_VENUE][venue.id][self.KEY_SLOT]:
            self.examtts[self.KEY_VENUE][venue.id][self.KEY_SLOT][slot.id] = {}

    def add_module(self, slot_venue_obj, venue_slot_obj, module, student):
        self.add_module_to_obj(slot_venue_obj, module, student)
        self.add_module_to_obj(venue_slot_obj, module, student)

    def add_module_to_obj(self, obj, module, student):
        if module.code not in obj:
            obj[module.code] = []
        obj[module.code].append({
            "name": student.name,
            self.KEY_LIFEGROUP: student.lifegroup})
