class JumpInstruction:
    comparisons = {
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '>=': lambda x, y: x >= y,
        '>': lambda x, y: x > y,
        '!=': lambda x, y: x != y,
    }

    def __init__(self, input_string: str):
        tokens = input_string.split()
        self.target_register = tokens[0]
        self.update_direction = 1 if tokens[1] == 'inc' else -1
        self.update_amplitude = int(tokens[2])
        # ignore token[3] which is always 'if'
        self.condition_register = tokens[4]
        self.condition_operator = tokens[5]
        self.condition_operand = int(tokens[6])

    def condition_satisfied(self, register_value):
        return self.comparisons[self.condition_operator](register_value, self.condition_operand)

    def debug(self):
        print(self.target_register,
              self.update_direction,
              self.update_amplitude,
              self.condition_register,
              self.condition_operator,
              self.condition_operand)


class Registers:
    _registers = {}

    def read(self, register_key: str):
        if register_key not in self._registers:
            self.write(register_key, 0)
        return self._registers[register_key]

    def write(self, register_key: str, value: int):
        self._registers[register_key] = value

    def debug(self):
        print(self._registers)

    def print_largest_value(self):
        print(sorted(list(self._registers.values()), reverse=True)[0])


registers = Registers()

# with open('example-input.txt') as file:
with open('input.txt') as file:
    for line in file:
        jump_instruction = JumpInstruction(line)

        value_of_condition_register = registers.read(jump_instruction.condition_register)
        if jump_instruction.condition_satisfied(value_of_condition_register):

            current_value = registers.read(jump_instruction.target_register)
            new_value = current_value + jump_instruction.update_amplitude * jump_instruction.update_direction

            registers.write(jump_instruction.target_register, new_value)

registers.debug()
registers.print_largest_value()
