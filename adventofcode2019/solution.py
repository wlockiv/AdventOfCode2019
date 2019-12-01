# Template class to be inherited for each day's solution.

class Solution:
    def __init__(self, input_file, test_input=None):
        """
        Boilerplate class for each day's solution. Import this class to inherit its basic methods.
        """
        self.input_file = input_file
        self.parsed_input = self.parse_input_file() if test_input is None else self.parse_raw(test_input)
        # self.__solution = None

    def parse_input_file(self):
        with open(self.input_file) as file:
            raw_input = file.read()
        return self.parse_raw(raw_input)

    @staticmethod
    def parse_raw(raw_input):
        input_list = raw_input.split('\n')
        return [int(i) for i in input_list]

    @property
    def solution(self):
        return None
