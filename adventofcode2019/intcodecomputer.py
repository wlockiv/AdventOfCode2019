from enum import Enum
from typing import List, Optional, Any, Tuple


class Modes:
    POSITION = 0
    IMMEDIATE = 1


class Status(Enum):
    INITIALIZED = 0
    RUNNING = 1
    PAUSED = 2
    DONE = 3


class IntcodeComputer:
    status: Status
    output: List[int]

    def __init__(self, program: List[int], phase_code: Optional[int] = None, feedback: bool = False):
        self.__memory = program
        self.feedback = feedback
        self.phase_code = phase_code
        self.pointer = 0
        self.inputs = [1]
        self.output = []
        self.opcode_map = {
            1: self.__opcode_1,
            2: self.__opcode_2,
            3: self.__opcode_3,
            4: self.__opcode_4,
            5: self.__opcode_5,
            6: self.__opcode_6,
            7: self.__opcode_7,
            8: self.__opcode_8,
            99: self.__opcode_99
        }
        self.status = Status.INITIALIZED

    @property
    def memory(self):
        return self.__memory

    @property
    def parsed_opcode(self) -> Tuple[int, int, int]:
        code_str = str(self.__memory[self.pointer]).zfill(4)
        opcode = int(code_str[-2:])
        mode_1 = int(code_str[-3])
        mode_2 = int(code_str[0])
        return opcode, mode_1, mode_2

    def __get_values(self, parameters: List[int], modes: List[int]) -> List[int]:
        """
        Identifies the values with respect to position or immediate mode

        Parameters:
        parameters (list): Parameters of the instruction.
        """
        values = []
        for i in range(len(parameters) - 1):
            values.append(self.__memory[parameters[i]] if modes[i] == Modes.POSITION else parameters[i])
        return values

    def __opcode_1(self, modes: List[int]):
        """Adds the parameter values in either position or immediate mode"""
        instruction = self.__memory[self.pointer: self.pointer + 4]
        parameters = instruction[1:]
        val_1, val_2 = self.__get_values(parameters, modes)
        out_pos = parameters[2]
        self.__memory[out_pos] = val_1 + val_2
        self.pointer += len(instruction)

    def __opcode_2(self, modes: List[int]):
        """Multiplies the parameter values in either position or immediate mode"""
        instruction = self.__memory[self.pointer: self.pointer + 4]
        parameters = instruction[1:]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.__memory[parameters[2]] = val_1 * val_2
        self.pointer += len(instruction)

    def __opcode_3(self):
        """Writes usr_input to the address indicated by its only parameter"""
        instruction = self.__memory[self.pointer:self.pointer + 2]
        out_pos = instruction[1]
        self.__memory[out_pos] = self.inputs.pop(0)
        self.pointer += len(instruction)

    def __opcode_4(self, modes: List[int]):
        """Outputs the diagnostic code located at its only parameter in either position or immediate mode"""
        instruction = self.__memory[self.pointer:self.pointer + 2]
        parameter = instruction[1]
        val = self.__memory[parameter] if modes[0] == Modes.POSITION else parameter
        self.output.append(val)
        self.pointer += len(instruction)
        if self.feedback:
            self.status = Status.PAUSED

    def __opcode_5(self, modes: List[int]):
        """Jump if true"""
        # This may need to be updated as the instruction only had 2 params, but this should keep it working with the
        # __get_values function for now
        parameters = self.__memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        if val_1:
            self.pointer = val_2
        else:
            self.pointer += 3

    def __opcode_6(self, modes: List[int]):
        """Jump if false"""
        # This may need to be updated as the instruction only had 2 params, but this should keep it working with the
        # __get_values function for now
        parameters = self.__memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        if not val_1:
            self.pointer = val_2
        else:
            self.pointer += 3

    def __opcode_7(self, modes: List[int]):
        """Less than"""
        instruction = self.__memory[self.pointer:self.pointer + 4]
        parameters = instruction[1:]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.__memory[parameters[2]] = 1 if val_1 < val_2 else 0
        self.pointer += len(instruction)

    def __opcode_8(self, modes: List[int]):
        """Equals"""
        instruction = self.__memory[self.pointer:self.pointer + 4]
        parameters = instruction[1:]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.__memory[parameters[2]] = 1 if val_1 == val_2 else 0
        self.pointer += len(instruction)

    def __opcode_99(self):
        self.status = Status.DONE

    def __run_opcode(self, opcode_num, modes):
        mode_opcodes = (1, 2, 4, 5, 6, 7, 8)
        try:
            opcode_fn = self.opcode_map[opcode_num]
            if opcode_num in mode_opcodes:
                opcode_fn(modes)
            else:
                opcode_fn()
        except KeyError:
            raise Exception(f'{opcode_num} is not a valid opcode.')

    def run_program(self, inputs=None, diagnostic=True):
        if inputs:
            self.inputs = inputs

        if self.phase_code is not None and self.status == Status.INITIALIZED:
            self.inputs.insert(0, self.phase_code)

        if self.status in (Status.INITIALIZED, Status.PAUSED):
            self.status = Status.RUNNING
        elif self.status == Status.DONE:
            raise Exception('This machine has been terminated with Opcode 99. Cannot run the program.')

        while self.status == Status.RUNNING and self.pointer < len(self.__memory):
            opcode, *modes = self.parsed_opcode
            self.__run_opcode(opcode, modes)

        return self.output if diagnostic else self.output[-1]


class AmpController:
    def __init__(self, program, phase_codes, feedback_loop=False):
        self.amplifiers = [IntcodeComputer(program.copy(), pc, feedback_loop) for pc in phase_codes]
        self.phase_codes = phase_codes
        self.output_signal = 0

    def run_battery(self):
        while self.amplifiers[-1].status != Status.DONE:
            for amp in self.amplifiers:
                amp.run_program([self.output_signal], diagnostic=False)
                self.output_signal = amp.output[-1]
