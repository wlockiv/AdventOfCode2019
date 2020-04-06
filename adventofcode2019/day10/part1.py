import math
import os

from adventofcode2019.solution import Solution


class Day10P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day10P1, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def parse_raw(raw_input):
        return raw_input

    def get_asteroid_coords(self):
        asteroid_rows = self.parsed_input.split('\n')
        asteroid_coords = set()
        for y, row in enumerate(asteroid_rows):
            for x, value in enumerate(row):
                if value == '#':
                    asteroid_coords.add((x, y))
        return asteroid_coords

    @staticmethod
    def calc_point_deltas(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x2 - x1, y2 - y1

    @property
    def solution(self):
        asteroid_coords = self.get_asteroid_coords()
        stations_with_coverage = {(x, y): 0 for x, y in asteroid_coords}

        for coord1 in asteroid_coords:
            slopes = set()
            for coord2 in asteroid_coords:
                dx, dy = self.calc_point_deltas(coord1, coord2)
                if coord1 != coord2:
                    gcd = math.gcd(dx, dy)
                    dx, dy = dx // gcd, dy // gcd
                    slopes.add((dx, dy))
            stations_with_coverage[coord1] += len(slopes)

        return max(stations_with_coverage.values())


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day10P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 10: Part 1')
    print(f'\tSolution: {solve()}')
