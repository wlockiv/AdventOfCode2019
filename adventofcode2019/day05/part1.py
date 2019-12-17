import os

from adventofcode2019.solution import Solution
from adventofcode2019.intcode.intcodecomputer import IntcodeComputer


class Day05P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day05P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_test(test_input):
        return [int(i) for i in test_input.split(',')]

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    @property
    def solution(self):
        computer = IntcodeComputer(self.parsed_input.copy(), 1)
        return computer.run_diagnostic()[-1]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day05P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 05: Part 1')
    print(f'\tSolution: {solve()}')
