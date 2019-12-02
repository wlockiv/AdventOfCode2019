import os

from adventofcode2019.solution import Solution


class Day02P1(Solution):
    pass


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day02P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
