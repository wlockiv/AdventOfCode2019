import math
import os

from adventofcode2019.solution import Solution


class Day06P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day06P1, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def parse_raw(raw_input):
        # orbits will be represented by {"child": "parent"}
        orbit_dict = {}
        for i in raw_input.split('\n'):
            parent, child = i.split(')')
            orbit_dict[child] = parent
        return orbit_dict

    def trace_orbit(self, origin, destination='COM'):
        child = origin
        orbit_chain = []
        while True:
            if (next_child := self.parsed_input[child]) != destination:
                child = next_child
                orbit_chain.append(next_child)
            else:
                orbit_chain.append(next_child)
                break
        return orbit_chain

    @property
    def solution(self):
        total_orbits = 0
        for origin_child in self.parsed_input.keys():
            total_orbits += len(self.trace_orbit(origin_child))

        return total_orbits


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day06P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 06: Part 1')
    print(f'\tSolution: {solve()}')
