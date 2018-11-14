from ..api.app import db


class Storage:

    def exists_student(self, student):
        return self.exists(student, student.name)

    def exists_module(self, module):
        return self.exists(module, module.code)

    def exists_slot(self, slot):
        return self.exists(slot)

    def exists(self, target, value=None):
        return target.__class__ \
            .query.get(value if value is not None else target.id) \
            .scalar() is not None

    def insert_student(self, student):
        db.session.add(student)

    def insert_module(self, module):
        db.session.add(module)
