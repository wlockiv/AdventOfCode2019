import math
import os

from adventofcode2019.solution import Solution


class Day01P1(Solution):
    def __init__(self, test_input=None):
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file = os.path.join(location, 'input')
        super(Day01P1, self).__init__(input_file, test_input=test_input)
        self.mass_list = [Module(mass) for mass in self.parsed_input]

    @property
    def solution(self):
        return sum([mod.fuel_needed() for mod in self.mass_list])


class Module:
    def __init__(self, mass):
        self.mass = mass

    def fuel_needed(self):
        return math.floor(self.mass / 3) - 2


def solve(test_input=None):
    return Day01P1(test_input).solution


if __name__ == '__main__':
    print(f'Day 01: Part 1')
    print(f'\tSolution: {solve()}')
