import os
import itertools

from adventofcode2019.day05._part1 import Day05P1 as IntcodeComputer


class Day07P1(IntcodeComputer):
    def __init__(self, input_file='input', test_input=None):
        super(Day07P1, self).__init__(input_file, test_input=test_input)

    @staticmethod
    def run_diagnostic(data, inputs):
        start = 0
        end = 4 if Day07P1.parse_opcode(data[0])[0] in (1, 2) else 2
        test_results = []

        while True:
            current_slice = data[start:end]
            opc, mode_1, mode_2 = Day07P1.parse_opcode(current_slice[0])
            if opc == 99:
                break

            if opc in (1, 2, 7, 8):
                val_1 = current_slice[1] if mode_1 else data[current_slice[1]]
                val_2 = current_slice[2] if mode_2 else data[current_slice[2]]
                out_pos = current_slice[3]
                if opc == 1:
                    data[out_pos] = val_1 + val_2
                elif opc == 2:
                    data[out_pos] = val_1 * val_2
                elif opc == 7:
                    data[out_pos] = 1 if val_1 < val_2 else 0
                elif opc == 8:
                    data[out_pos] = 1 if val_1 == val_2 else 0
                start += 4
            elif opc in (3, 4):
                out_pos = current_slice[1]
                if opc == 3:
                    if len(inputs) == 0:
                        raise Exception('No input!')
                    data[out_pos] = inputs.pop(0)
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

            if (next_opc := Day07P1.parse_opcode(data[start])[0]) in (1, 2, 7, 8):
                end = start + 4
            elif next_opc in (3, 4):
                end = start + 20
            elif next_opc in (5, 6):
                end = start + 3
        return test_results

    @property
    def solution(self, input_signal=0):
        max_thruster_signal = 0
        phase_perms = [list(perm) for perm in itertools.permutations(range(5))]
        for perm in phase_perms:
            output = 0
            while len(perm) > 0:
                output = self.run_diagnostic(self.parsed_input.copy(), [perm.pop(0), output])[-1]
            max_thruster_signal = max(max_thruster_signal, output)
        return max_thruster_signal


def solve(test_input=None):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    input_file = os.path.join(location, 'input')

    return Day07P1(input_file, test_input).solution


if __name__ == '__main__':
    print(f'Day 07: Part 1')
    print(f'\tSolution: {solve()}')
