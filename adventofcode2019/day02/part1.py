import os

from adventofcode2019.solution import Solution
from adventofcode2019.intcode.intcodecomputer import IntcodeComputer


class Day02P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day02P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_test(test_input):
        return [int(i) for i in test_input.split(',')]

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    @property
    def solution(self):
        modified_input = self.parsed_input.copy()
        # Input modified per instruction
        modified_input[1] = 12
        modified_input[2] = 2
        computer = IntcodeComputer(modified_input)
        computer.run_program()
        return computer.memory[0]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day02P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
