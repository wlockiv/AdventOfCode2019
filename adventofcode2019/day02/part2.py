import os

from adventofcode2019.day02.part1 import Day02P1
from adventofcode2019.intcodecomputer import IntcodeComputer


class Day02P2(Day02P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day02P2, self).__init__(input_file, test_input)

    @property
    def solution(self):
        target = 19690720
        for noun in range(100):
            for verb in range(100):
                modified_input = self.parsed_input.copy()
                modified_input[1], modified_input[2] = noun, verb
                computer = IntcodeComputer(modified_input)
                computer.run_program()
                if computer.memory[0] == target:
                    return 100 * noun + verb
        return None


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day02P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 2')
    print(f'\tSolution: {solve()}')
