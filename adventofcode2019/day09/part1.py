import os
import itertools

from adventofcode2019.day07._part1 import Day07P1 as IntcodeComputer


class Day09P1(IntcodeComputer):
    def __init__(self, input_file='input', test_input=None):
        super(Day09P1, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def run_diagnostic(data, inputs):
        start = 0
        end = 4 if Day09P1.parse_opcode(data[0])[0] in (1, 2) else 2
        rel_base = 0
        test_results = []

        while True:
            current_slice = data[start:end]
            opc, mode_1, mode_2 = Day09P1.parse_opcode(current_slice[0])
            if opc == 99:
                break

            get_index = lambda p: p % len(data)

            # All intcode instructions with 4 params
            if opc in (1, 2, 7, 8):
                val_1 = data[get_index(current_slice[1])] if mode_1 == 0 else current_slice[1] if mode_1 == 1 else data[
                    get_index(current_slice[1]) + rel_base]
                val_2 = data[get_index(current_slice[2])] if mode_2 == 0 else current_slice[1] if mode_1 == 1 else data[
                    get_index(current_slice[1]) + rel_base]
                out_pos = get_index(current_slice[3])
                if opc == 1:
                    data[out_pos] = val_1 + val_2
                elif opc == 2:
                    data[out_pos] = val_1 * val_2
                elif opc == 7:
                    data[out_pos] = 1 if val_1 < val_2 else 0
                elif opc == 8:
                    data[out_pos] = 1 if val_1 == val_2 else 0
                start += 4
            elif opc in (3, 4, 9):
                val = get_index(current_slice[1])
                if opc == 3:
                    if len(inputs) == 0:
                        raise Exception('No input!')
                    data[val] = inputs.pop(0)
                elif opc == 4:
                    test_results.append(data[val])
                elif opc == 9:
                    rel_base += val
                start += 2
            elif opc in (5, 6):
                val_1 = data[get_index(current_slice[1])] if mode_1 == 0 else current_slice[1] if mode_1 == 1 else data[
                    get_index(current_slice[1]) + rel_base]
                val_2 = data[get_index(current_slice[2])] if mode_2 == 0 else current_slice[1] if mode_1 == 1 else data[
                    get_index(current_slice[1]) + rel_base]
                if opc == 5 and val_1:
                    start = val_2
                elif opc == 6 and not val_1:
                    start = val_2
                else:
                    start += 3

            if (next_opc := Day09P1.parse_opcode(data[start])[0]) in (1, 2, 7, 8):
                end = start + 4
            elif next_opc in (3, 4):
                end = start + 20
            elif next_opc in (5, 6):
                end = start + 3
            elif next_opc == 99:
                break
        return test_results

    @property
    def solution(self):
        return self.run_diagnostic(self.parsed_input.copy(), [1])


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day09P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 07: Part 1')
    print(f'\tSolution: {solve()}')
