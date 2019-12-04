import os

from adventofcode2019.solution import Solution
import re


class Day04P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day04P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_raw(raw_input):
        start, finish = [int(i) for i in raw_input.split('-')]
        return set(range(start, finish + 1))

    @property
    def solution(self):
        answer = []
        for n in self.parsed_input:
            if re.search(r'^(?=\d*$)1*2*3*4*5*6*7*8*9*$', str(n)) and re.search(r'(\d)\1+', str(n)):
                answer.append(n)

        return len(answer)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day04P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 04: Part 1')
    print(f'\tSolution: {solve()}')
