import os

from adventofcode2019.solution import Solution


class Day02P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day02P1, self).__init__(input_file, test_input)
        # restoring the gravity assist program
        self.parsed_input[1] = 12
        self.parsed_input[2] = 2


    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    def opcode_1(self, input_slice):
        val_1 = self.parsed_input[input_slice[1]]
        val_2 = self.parsed_input[input_slice[2]]
        output_pos = input_slice[3]

        self.parsed_input[output_pos] = val_1 + val_2

    def opcode_2(self, current_list):
        val_1 = self.parsed_input[current_list[1]]
        val_2 = self.parsed_input[current_list[2]]
        output_pos = current_list[3]

        self.parsed_input[output_pos] = val_1 * val_2

    @property
    def solution(self):
        start = 0
        end = 4

        while True:
            current_list = self.parsed_input[start:end]
            if current_list[0] == 1:
                self.opcode_1(current_list)
            elif current_list[0] == 2:
                self.opcode_2(current_list)
            elif current_list[0] == 99:
                break
            start += 4
            end += 4

        return self.parsed_input[0]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day02P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
