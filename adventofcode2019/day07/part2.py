import os
from itertools import permutations

from adventofcode2019.day07.part1 import Day07P1
from adventofcode2019.intcodecomputer import AmpController


class Day07P2(Day07P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day07P2, self).__init__(input_file, test_input)

    @property
    def solution(self):
        max_signal = 0
        phase_code_perms = permutations(range(5, 10))
        for perm in phase_code_perms:
            amp_controller = AmpController(self.parsed_input.copy(), perm, True)
            amp_controller.run_battery()
            max_signal = max(max_signal, amp_controller.output_signal)

        return max_signal


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day07P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 07: Part 2')
    print(f'\tSolution: {solve()}')
