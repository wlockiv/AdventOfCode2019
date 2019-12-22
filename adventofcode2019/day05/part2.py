import os

from adventofcode2019.day05.part1 import Day05P1
from adventofcode2019.intcodecomputer import IntcodeComputer


class Day05P2(Day05P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day05P2, self).__init__(input_file, test_input)

    @property
    def solution(self):
        computer = IntcodeComputer(self.parsed_input.copy())
        return computer.run_program([5])[0]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day05P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 05: Part 1')
    print(f'\tSolution: {solve()}')
