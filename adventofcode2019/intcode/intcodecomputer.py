from typing import List, Iterable


class Program:
    def __init__(self, program: List[int]):
        self.program = program.copy()
        self.output = []
        self.pointer = 0

    def get_values(self) -> Iterable[int]:
        param_1, param_2, out_pos = self.program[self.pointer + 1: self.pointer + 4]
        return self.program[param_1], self.program[param_2], out_pos

    def get_opcode(self):
        return self.program[self.pointer]

    def opcode_1(self):
        val_1, val_2, out_pos = self.get_values()
        self.program[out_pos] = val_1 + val_2
        self.pointer += 4

    def opcode_2(self):
        val_1, val_2, out_pos = self.get_values()
        self.program[out_pos] = val_1 + val_2
        self.point += 4

    def opcode_99(self):
        return self.output


class IntcodeComputer:
    def __init__(self, program_input):
        self.program = Program(program_input.copy())
        self.opc_map = {
            1: self.program.opcode_1,
            2: self.program.opcode_2,
            99: self.program.opcode_99
        }

    def run_opcode(self, opcode: int):
        try:
            self.opc_map[opcode]()
        except KeyError:
            print(f'Opcode {opcode} doesn\'t has not been mapped')

    def run_program(self):
        while self.program.pointer < len(self.program.program):
            opcode = self.program.get_opcode()
            if opc == 99:
                return self.program.program[0]

            self.run_opcode(opcode)


class ProgramInput(list):
    pass
