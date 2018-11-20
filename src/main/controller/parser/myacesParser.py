import logging
import os
from .parser import Parser
from .parserResult import ParserResult


class MyacesParser(Parser):
    name_regex = r"""Name:\s([A-Za-z \-,_]+)\b"""
    examtt_regex = r"""
        (([A-Z0-9]+)\s+Module\sCode:\s+\2\s+Venue:\s+([A-Z0-9-_]+)\s+Date:
        \s+([0-9]{2}[A-Z]{3})\s+Time:\s+([0-9]{4})HR)"""
    
    GROUPNUM_NAME = 1
    GROUPNUM_MODULE_CODE = 2
    GROUPNUM_VENUE = 3
    GROUPNUM_DATE = 4
    GROUPNUM_TIME = 5

    PATH_LOG = os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../../../logs/myacesParser.log'))
    logging.basicConfig(filename=PATH_LOG, level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def __init__(self):
        super().__init__(self.examtt_regex, self.name_regex)

    def parse(self, examtt_str):
        logging.debug("Parsing Examtt String: {}".format(examtt_str))
        return super().parse(examtt_str)

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
