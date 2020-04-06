import os

from adventofcode2019.day04.part1 import Day04P1
import re


class Day04P2(Day04P1):
    def __init__(self, input_file='input', test_input=None):
        super(Day04P2, self).__init__(input_file, test_input)

    @property
    def solution(self):
        answer = []
        for n in self.parsed_input:
            n_str = str(n)
            if re.search(r'^(?=\d*$)1*2*3*4*5*6*7*8*9*$', n_str) and (matches := re.findall(r'(\d)\1+', n_str)):
                if any((n_str.count(m) == 2) for m in matches):
                    answer.append(n)

        return len(answer)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day04P2(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 04: Part 2')
    print(f'\tSolution: {solve()}')
