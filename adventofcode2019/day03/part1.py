import os

from adventofcode2019.solution import Solution
from adventofcode2019.day03.grid import Grid


class Day03P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day03P1, self).__init__(input_file, test_input)
        self.w1, self.w2 = self.parsed_input

    @staticmethod
    def parse_raw(raw_input):
        wires = [w.split(',') for w in raw_input.split('\n')]
        w1 = [{'dir': i[0], 'dist': int(i[1:])} for i in wires[0]]
        w2 = [{'dir': i[0], 'dist': int(i[1:])} for i in wires[1]]
        return [w1, w2]

    @property
    def solution(self):
        w1_grid = Grid()
        [w1_grid.walk(length['dir'], length['dist']) for length in self.w1]

        w2_grid = Grid()
        [w2_grid.walk(length['dir'], length['dist']) for length in self.w2]

        intersects = set(w1_grid.points.keys() & w2_grid.points.keys())
        return min([Grid.manhattan_dist((0, 0), p) for p in intersects])


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day03P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
