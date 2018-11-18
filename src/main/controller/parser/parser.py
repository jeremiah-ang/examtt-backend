import re


class Parser:
    def __init__(self, examtt_regex, name_regex):
        self.examtt_regex = examtt_regex
        self.name_regex = name_regex

    def parse(self, examtt_str):
        '''
        Parse the examtt string
        returns a ParserResult Object
        '''
        examtt_matches = re.finditer(
            self.examtt_regex, examtt_str, re.MULTILINE | re.VERBOSE)
        name_matches = re.search(
            self.name_regex, examtt_str, re.VERBOSE)
        return self.process_matches(examtt_matches, name_matches)

    def process_matches(self, examtt_matches, name_matches):
        '''
        Process the matches
        To be implemented by subclasses
        returns a ParserResult Object
        '''
        raise NotImplementedError
