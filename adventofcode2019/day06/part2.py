import math
import os

from adventofcode2019.day06.part1 import Day06P1


class Day06P2(Day06P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day06P2, self).__init__(input_file, test_input=test_input)

    def get_transfers(self, origin="YOU", destination="SAN"):
        origin_path = self.trace_orbit(origin)
        destination_path = self.trace_orbit(destination)
        cross_point = [p for p in origin_path if p in destination_path][0]
        return self.trace_orbit(origin, cross_point) + self.trace_orbit(destination, cross_point)[:-1]

    @property
    def solution(self, origin=None, destination="COM"):
        return len(self.get_transfers("YOU", "SAN")) - 1


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day06P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 06: Part 2')
    print(f'\tSolution: {solve()}')
