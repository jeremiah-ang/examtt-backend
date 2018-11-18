from .parser import Parser
from .parserResult import ParserResult


class ExamttParser(Parser):

    KEY_NAME = "name"
    KEY_MODULES = "modules"
    KEY_MODULE_CODE = "module_code"
    KEY_VENUE = "venue"
    KEY_DATE = "date"
    KEY_TIME = "time"

    def __init__(self):
        super().__init__("", "")

    def parse(self, examtt_obj):
        name = examtt_obj[self.KEY_NAME]
        parserResult = ParserResult(name)
        modules = examtt_obj[self.KEY_MODULES]
        for module in modules:
            module_code = module[self.KEY_MODULE_CODE]
            venue = module[self.KEY_VENUE]
            date = module[self.KEY_DATE]
            time = module[self.KEY_TIME]
            print(module, venue, date, time)
            parserResult.add_entry(module_code, venue, date, time)
        return parserResult
