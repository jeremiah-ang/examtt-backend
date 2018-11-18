from .parser import Parser
from .parserResult import ParserResult


class MyacesParser(Parser):
    name_regex = r"""Name:\s([A-Z\s-]+)\s\b"""
    examtt_regex = r"""
        (([A-Z0-9]+)\s+Module\sCode:\s+\2\s+Venue:\s+([A-Z0-9-]+)\s+Date:
        \s+([0-9]{2}[A-Z]{3})\s+Time:\s+([0-9]{4})HR)"""
    
    GROUPNUM_NAME = 1
    GROUPNUM_MODULE_CODE = 2
    GROUPNUM_VENUE = 3
    GROUPNUM_DATE = 4
    GROUPNUM_TIME = 5

    def __init__(self):
        super().__init__(self.examtt_regex, self.name_regex)

    def process_matches(self, examtt_matches, name_matches):
        name = name_matches.group(self.GROUPNUM_NAME)
        parserResult = ParserResult(name)

        for matchNum, match in enumerate(examtt_matches):
            module_code = match.group(self.GROUPNUM_MODULE_CODE)
            venue = match.group(self.GROUPNUM_VENUE)
            date = match.group(self.GROUPNUM_DATE)
            time = match.group(self.GROUPNUM_TIME)
            parserResult.add_entry(module_code, venue, date, time)

        return parserResult
