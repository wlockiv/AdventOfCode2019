import math
import os

from adventofcode2019.day01.part1 import Module as P1Module
from adventofcode2019.solution import Solution


class Day01P2(Solution):
    def __init__(self, test_input=None):
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file = os.path.join(location, 'input')
        super(Day01P2, self).__init__(input_file, test_input=test_input)
        self.mass_list = [Module(mass) for mass in self.parsed_input]

    @property
    def solution(self):
        # return sum([mod.fuel_needed() for mod in self.mass_list])
        return sum([mod.fuel_needed() for mod in self.mass_list])


class Module(P1Module):
    def __init__(self, mass):
        super(Module, self).__init__(mass)

    @staticmethod
    def fuel_formula(fuel_or_mass):
        return math.floor(fuel_or_mass / 3) - 2

    def fuel_needed(self):
        result = [self.fuel_formula(self.mass)]
        while True:
            requirement = self.fuel_formula(result[-1])

            if requirement > 0:
                result.append(requirement)
            else:
                break
        return sum(result)


def solve(test_input=None):
    return Day01P2(test_input).solution


if __name__ == '__main__':
    print(f'Day 01: Part 2')
    print(f'\tSolution: {solve()}')
