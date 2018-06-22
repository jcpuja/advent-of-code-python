# After unsuccessful attempts, copied solution from
# https://old.reddit.com/r/adventofcode/comments/7kj35s/2017_day_18_solutions/dretdd8/
# N.B. No deadlock detection is performed, I was just lucky with my puzzle input.
# Some solutions with deadlock detection can be found on that reddit thread

import collections
import multiprocessing.pool
import queue

file_name = 'input.txt'
with open(file_name) as f:
    PROGRAM = [l.rstrip() for l in f]


def run(ident, inqueue, outqueue):
    regs = collections.defaultdict(int)
    regs['p'] = ident

    def val(v):
        try:
            return int(v)
        except ValueError:
            return regs[v]

    pc = 0
    count = 0
    played = None

    while 0 <= pc < len(PROGRAM):
        cmd = PROGRAM[pc].split()
        if cmd[0] == 'snd':
            played = val(cmd[1])
            if outqueue:
                outqueue.put(val(cmd[1]))
            count += 1
        elif cmd[0] == 'set':
            regs[cmd[1]] = val(cmd[2])
        elif cmd[0] == 'add':
            regs[cmd[1]] += val(cmd[2])
        elif cmd[0] == 'mul':
            regs[cmd[1]] *= val(cmd[2])
        elif cmd[0] == 'mod':
            regs[cmd[1]] %= val(cmd[2])
        elif cmd[0] == 'rcv':
            if inqueue:
                try:
                    regs[cmd[1]] = inqueue.get(timeout=5)
                except queue.Empty:
                    return count
            elif regs[cmd[1]] != 0:
                return played
        elif cmd[0] == 'jgz':
            if val(cmd[1]) > 0:
                pc += val(cmd[2])
                continue
        pc += 1

    return count


print('PART 1:', run(0, None, None))

pool = multiprocessing.pool.ThreadPool(processes=2)

q1 = multiprocessing.Queue()
q2 = multiprocessing.Queue()

res1 = pool.apply_async(run, (0, q1, q2))
res2 = pool.apply_async(run, (1, q2, q1))

res1.get()
print('PART 2:', res2.get())
