import os

from adventofcode2019.solution import Solution


class Day03P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day03P1, self).__init__(input_file, test_input)
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


class Grid:
    def __init__(self, origin=(0, 0)):
        self.grid = {origin: 1}
        self.pos = origin

    @property
    def points(self):
        return self.grid.keys()

    def __iter__(self):
        return self.grid

    def step(self, direction):
        x, y = self.pos
        x_step = 1 if direction == 'R' else -1 if direction == 'L' else 0
        y_step = 1 if direction == 'U' else -1 if direction == 'D' else 0
        next_pos = (x + x_step, y + y_step)

        self.grid.setdefault(next_pos, 0)
        self.grid[next_pos] += 1

        self.pos = next_pos

    def walk(self, direction, dist):
        x, y = self.pos
        for step in range(1, dist + 1):
            self.step(direction)

    @staticmethod
    def manhattan_dist(point_1, point_2):
        x_1, y_1 = point_1
        x_2, y_2 = point_2
        return abs(x_2 - x_1) + abs(y_2 - y_1)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day03P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
