import os

from adventofcode2019.solution import Solution


class Day02P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day02P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    def opcode_1(self, input_slice):
        val_1 = self.parsed_input[input_slice[1]]
        val_2 = self.parsed_input[input_slice[2]]
        output_pos = input_slice[3]

        self.parsed_input[output_pos] = val_1 + val_2

    def opcode_2(self, input_slice):
        val_1 = self.parsed_input[input_slice[1]]
        val_2 = self.parsed_input[input_slice[2]]
        output_pos = input_slice[3]

        self.parsed_input[output_pos] = val_1 * val_2

    @staticmethod
    def run_all_instruction(data, noun=12, verb=2):
        start, end = 0, 4
        data[1] = noun
        data[2] = verb

        while True:
            current_slice = data[start:end]
            instruction = current_slice[0]
            val_1, val_2 = data[current_slice[1]], data[current_slice[2]]
            out_pos = current_slice[3]
            if instruction == 1:
                data[out_pos] = val_1 + val_2
            elif instruction == 2:
                data[out_pos] = val_1 * val_2
            elif instruction == 99:
                break
            start += 4
            end += 4

        return data[0]

    @property
    def solution(self):
        return self.run_all_instruction(self.parsed_input)


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day02P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 02: Part 1')
    print(f'\tSolution: {solve()}')
