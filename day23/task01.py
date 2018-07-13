def run_program(file_name):
    with open(file_name) as f:
        instructions = [line.strip().split() for line in f]

    registers = {}
    for r in list('abcdefgh'):
        registers[r] = 0
    cursor = 0
    multiplications = 0

    def val(v):
        try:
            return int(v)
        except ValueError:
            return registers[v]

    while 0 <= cursor < len(instructions):
        cmd = instructions[cursor]
        if cmd[0] == 'set':
            registers[cmd[1]] = val(cmd[2])
            cursor += 1

        elif cmd[0] == 'sub':
            registers[cmd[1]] -= val(cmd[2])
            cursor += 1

        elif cmd[0] == 'mul':
            registers[cmd[1]] *= val(cmd[2])
            cursor += 1
            multiplications += 1

        elif cmd[0] == 'jnz':
            offset = val(cmd[2]) if val(cmd[1]) != 0 else 1
            cursor += offset

    print(multiplications)


run_program('input.txt')
