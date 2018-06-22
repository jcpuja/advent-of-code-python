import re


class Duet:
    def __init__(self, _instructions):
        self.instructions = _instructions
        self.registers = {}
        self.register_pattern = re.compile('[a-z]')
        self.last_played_sound = None
        self.recovered = False
        self.terminated = False
        self.cursor = 0

    def register_get(self, register_key):
        if register_key not in self.registers:
            self.registers[register_key] = 0
        return self.registers[register_key]

    def get_arg_value(self, _operand):
        if self.register_pattern.match(_operand):
            return self.register_get(_operand)
        return int(_operand)

    def jump(self, steps=1):
        self.cursor += steps
        if self.cursor < 0 or self.cursor >= len(self.instructions):
            self.terminated = True

    def snd(self, args):
        arg, = args
        self.last_played_sound = self.get_arg_value(arg)
        self.jump()

    def set(self, args):
        register, operand = args
        self.registers[register] = self.get_arg_value(operand)
        self.jump()

    def add(self, args):
        register, operand = args
        current_value = self.register_get(register)
        self.registers[register] = current_value + self.get_arg_value(operand)
        self.jump()

    def mul(self, args):
        register, operand = args
        current_value = self.register_get(register)
        self.registers[register] = current_value * self.get_arg_value(operand)
        self.jump()

    def mod(self, args):
        register, operand = args
        current_value = self.register_get(register)
        self.registers[register] = current_value % self.get_arg_value(operand)
        self.jump()

    def rcv(self, args):
        arg, = args
        if self.get_arg_value(arg) != 0:
            print(self.last_played_sound)
            self.recovered = True
        self.jump()

    def jgz(self, args):
        guard, offset = args
        jump_steps = self.get_arg_value(offset) if self.get_arg_value(guard) > 0 else 1
        self.jump(jump_steps)

    def execute(self):
        functions = {
            'snd': self.snd,
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'mod': self.mod,
            'rcv': self.rcv,
            'jgz': self.jgz,
        }

        while not self.terminated and not self.recovered:
            commands = self.instructions[self.cursor].split()
            functions[commands[0]](commands[1:])


# file_name = 'example_input.txt'
file_name = 'input.txt'
with open(file_name) as f:
    instructions = [l.rstrip() for l in f]

Duet(instructions).execute()
