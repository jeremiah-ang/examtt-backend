import unittest
from src.main.model.examtt import Entry, Examtt

class ExamttTest(unittest.TestCase):
    def test_parse(self):
        self.examtt = Examtt()
        self.assertEqual(self.examtt.parse("hello"), Entry("Jeremiah", "CS4234", "Optimisation Algorithm", "1300", "MPSH"))

if __name__ == '__main__':
    unittest.main()
