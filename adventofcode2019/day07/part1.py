import os
import itertools

from adventofcode2019.day05.part1 import Day05P1 as IntcodeComputer


class Day07P1(IntcodeComputer):
    def __init__(self, input_file='input', test_input=None):
        super(Day07P1, self).__init__(input_file, test_input=test_input)

    def run_amplifiers(self, data, sequence):
        input_signal = 0
        for code in sequence:
            self.run_diagnostic(data, code)

    @property
    def solution(self, input_signal=0):
        output_signals = []
        for perm in itertools.permutations(range(5)):
            output = 0
            for code in perm:
                output += sum([self.amplify(self.parsed_input, code)])
                output_signals.append(output)

        return max(output_signals)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day07P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 07: Part 1')
    print(f'\tSolution: {solve()}')
