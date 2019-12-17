from enum import Enum


class Program(list):
    def __init__(self, *args, **kwargs):
        super(Program, self).__init__(args[0])


class Modes:
    POSITION = 0
    IMMEDIATE = 1


class IntcodeComputer:
    def __init__(self, program, usr_input=1):
        self.memory = program
        self.pointer = 0
        self.usr_input = usr_input
        self.output = []
        self.opcode_map = {
            1: self.__opcode_1,
            2: self.__opcode_2,
            3: self.__opcode_3,
            4: self.__opcode_4,
            5: self.__opcode_5,
            6: self.__opcode_6,
            7: self.__opcode_7,
            8: self.__opcode_8
        }

    @property
    def parsed_opcode(self):
        code_str = str(self.memory[self.pointer]).zfill(4)
        opcode = int(code_str[-2:])
        mode_1 = int(code_str[-3])
        mode_2 = int(code_str[0])
        return opcode, mode_1, mode_2

    def __get_values(self, parameters, modes):
        """
        Identifies the values with respect to position or immediate mode

        Parameters:
        parameters (list): Parameters of the instruction.
        """
        values = []
        for i in range(len(parameters) - 1):
            values.append(self.memory[parameters[i]] if modes[i] == Modes.POSITION else parameters[i])
        return values

    def __opcode_1(self, modes):
        """Adds the parameter values in either position or immediate mode"""
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        out_pos = parameters[2]
        self.memory[out_pos] = val_1 + val_2
        self.pointer += 4

    def __opcode_2(self, modes):
        """Multiplies the parameter values in either position or immediate mode"""
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.memory[parameters[2]] = val_1 * val_2
        self.pointer += 4

    def __opcode_3(self, modes):
        """Writes usr_input to the address indicated by its only parameter"""
        out_pos = self.memory[self.pointer + 1]
        self.memory[out_pos] = self.usr_input
        self.pointer += 2

    def __opcode_4(self, modes):
        """Outputs the diagnostic code located at its only parameter in either position or immediate mode"""
        parameter = self.memory[self.pointer + 1]
        val = self.memory[parameter] if modes[0] == Modes.POSITION else parameter
        self.output.append(val)
        self.pointer += 2

    def __opcode_5(self, modes):
        """Jump if true"""
        # This may need to be updated as the instruction only had 2 params, but this should keep it working with the
        # __get_values function for now
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        if val_1:
            self.pointer = val_2
        else:
            self.pointer += 3

    def __opcode_6(self, modes):
        """Jump if false"""
        # This may need to be updated as the instruction only had 2 params, but this should keep it working with the
        # __get_values function for now
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        if not val_1:
            self.pointer = val_2
        else:
            self.pointer += 3

    def __opcode_7(self, modes):
        """Less than"""
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.memory[parameters[2]] = 1 if val_1 < val_2 else 0
        self.pointer += 4

    def __opcode_8(self, modes):
        """Equals"""
        parameters = self.memory[self.pointer + 1:self.pointer + 4]
        val_1, val_2 = self.__get_values(parameters, modes)
        self.memory[parameters[2]] = 1 if val_1 == val_2 else 0
        self.pointer += 4

    def opcode_99(self):
        return self.output

    def run_diagnostic(self):
        while self.pointer < len(self.memory):
            opcode, *modes = self.parsed_opcode
            if opcode == 99:
                return self.output
            else:
                self.opcode_map[opcode](modes)

    def run_program(self):
        while self.pointer < len(self.memory):
            opcode, *modes = self.parsed_opcode
            if opcode == 99:
                break
            else:
                self.opcode_map[opcode](modes)
        return None
