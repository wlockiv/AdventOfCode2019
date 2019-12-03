import os

from adventofcode2019.solution import Solution
from adventofcode2019.day03.part1 import Grid


class Day03P2(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day03P2, self).__init__(input_file, test_input)
        self.wire_1, self.wire_2 = self.parsed_input

    @staticmethod
    def parse_raw(raw_input):
        wires = [w.split(',') for w in raw_input.split('\n')]
        wire_1 = [{'dir': i[0], 'dist': int(i[1:])} for i in wires[0]]
        wire_2 = [{'dir': i[0], 'dist': int(i[1:])} for i in wires[1]]
        return [wire_1, wire_2]

    @property
    def solution(self):
        origin = (0, 0)
        wire_1_grid = Grid(origin)
        for length in self.wire_1:
            wire_1_grid.walk(length['dir'], length['dist'])

        wire_2_grid = Grid(origin)
        for length in self.wire_2:
            wire_2_grid.walk(length['dir'], length['dist'])

        intersects = [i for i in wire_1_grid.points if i in wire_2_grid.points and i != origin]
        intersect_distances = [Grid.manhattan_dist(origin, p) for p in intersects]
        return min(intersect_distances)



def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day03P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
