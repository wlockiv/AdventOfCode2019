import os
from itertools import permutations

from adventofcode2019.intcodecomputer import AmpController
from adventofcode2019.solution import Solution


class Day07P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day07P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_test(test_input):
        return [int(i) for i in test_input.split(',')]

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    @property
    def solution(self):
        max_signal = 0
        phase_code_perms = permutations(range(5))
        for perm in phase_code_perms:
            amp_controller = AmpController(self.parsed_input.copy(), perm)
            amp_controller.run_battery()
            max_signal = max(max_signal, amp_controller.output_signal)

        return max_signal


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day07P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 07: Part 1')
    print(f'\tSolution: {solve()}')
