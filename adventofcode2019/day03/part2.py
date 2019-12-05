import os

from adventofcode2019.day03.part1 import Day03P1, Grid


class Day03P2(Day03P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day03P2, self).__init__(input_file, test_input)
        self.w1, self.w2 = self.parsed_input

    @property
    def solution(self):
        w1_grid = Grid()
        [w1_grid.walk(length['dir'], length['dist']) for length in self.w1]

        w2_grid = Grid()
        [w2_grid.walk(length['dir'], length['dist']) for length in self.w2]

        intersects = set(w1_grid.points.keys() & w2_grid.points.keys())
        return min([w1_grid.points[i] + w2_grid.points[i] for i in intersects])


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day03P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
