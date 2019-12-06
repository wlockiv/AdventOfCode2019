import os
import sys

from adventofcode2019.solution import Solution


class Day05P1(Solution):
    def __init__(self, input_file='input', test_input=None):
        super(Day05P1, self).__init__(input_file, test_input)

    @staticmethod
    def parse_test(test_input):
        return [int(i) for i in test_input.split(',')]

    @staticmethod
    def parse_raw(raw_input):
        return [int(i) for i in raw_input.split(',')]

    @staticmethod
    def parse_opcode(opcode):
        o_str = str(opcode).zfill(4)
        return int(o_str[-2:]), int(o_str[-3]), int(o_str[-4])

    @staticmethod
    def run_diagnostic(data, usr_input=1):
        start = 0
        end = 4 if Day05P1.parse_opcode(data[0])[0] in (1, 2) else 2
        test_results = []

        while True:
            current_slice = data[start:end]
            opc, mode_1, mode_2 = Day05P1.parse_opcode(current_slice[0])
            if opc == 99:
                break

            if opc in (1, 2, 7, 8):
                val_1 = current_slice[1] if mode_1 else data[current_slice[1]]
                val_2 = current_slice[2] if mode_2 else data[current_slice[2]]
                out_pos = current_slice[3]
                # Add
                if opc == 1:
                    data[out_pos] = val_1 + val_2
                # Multiply
                elif opc == 2:
                    data[out_pos] = val_1 * val_2
                #
                elif opc == 7:
                    data[out_pos] = 1 if val_1 < val_2 else 0
                elif opc == 8:
                    data[out_pos] = 1 if val_1 == val_2 else 0
                start += 4
            elif opc in (3, 4):
                out_pos = current_slice[1]
                if opc == 3:
                    data[out_pos] = usr_input
                elif opc == 4:
                    test_results.append(data[out_pos])
                start += 2
            elif opc in (5, 6):
                val_1 = current_slice[1] if mode_1 else data[current_slice[1]]
                val_2 = current_slice[2] if mode_2 else data[current_slice[2]]
                if opc == 5 and val_1:
                    start = val_2
                elif opc == 6 and not val_1:
                    start = val_2
                else:
                    start += 3

            if (next_opc := Day05P1.parse_opcode(data[start])[0]) in (1, 2, 7, 8):
                end = start + 4
            elif next_opc in (3, 4):
                end = start + 20
            elif next_opc in (5, 6):
                end = start + 3
        return test_results

    @property
    def solution(self):
        return self.run_diagnostic(self.parsed_input)[-1]


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day05P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 05: Part 1')
    print(f'\tSolution: {solve()}')
