import os

from adventofcode2019.solution import Solution
from adventofcode2019.day03.part1 import Grid


class Day03P2(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day03P2, self).__init__(input_file, test_input)
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
        for length in self.w1:
            w1_grid.walk(length['dir'], length['dist'])

        w2_grid = Grid()
        for length in self.w2:
            w2_grid.walk(length['dir'], length['dist'])

        intersects = set(i for i in w1_grid.points if i in w2_grid.points and i != (0, 0))
        steps_to_intersects = {}

        for i in intersects:
            w1_steps = 0
            w1_grid.__init__()
            for length in self.w1:
                if w1_grid.walk_to_target(length['dir'], length['dist'], i):
                    w1_steps = w1_grid.step_count

            w2_steps = 0
            w2_grid.__init__()
            for length in self.w2:
                if w2_grid.walk_to_target(length['dir'], length['dist'], i):
                    w2_steps = w2_grid.step_count

            steps_to_intersects[i] = w1_steps + w2_steps

        return sorted(steps_to_intersects.items(), key=lambda kv: kv[1])[0][1]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day03P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
