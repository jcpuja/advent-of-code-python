# input_text = '0 2   7   0'
input_text = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'


def serialize_int_list(int_list):
    return ','.join([str(i) for i in int_list])


memory_banks = [int(n) for n in input_text.split()]

history = {}

steps = 0


while serialize_int_list(memory_banks) not in history:
    # Save serialized version of list in history map, with reference to the step where it was saved
    history[serialize_int_list(memory_banks)] = steps
    steps += 1

    # Find index of bank to redistribute
    cursor = memory_banks.index(max(memory_banks))
    left_to_redistribute = memory_banks[cursor]
    memory_banks[cursor] = 0

    while left_to_redistribute > 0:
        # Iterate over memory banks to redistribute blocks one by one
        cursor = (cursor + 1) % len(memory_banks)
        memory_banks[cursor] += 1
        left_to_redistribute -= 1

# Look up in history where we already found this state
step_where_duplicate_encountered = history[serialize_int_list(memory_banks)]

print(steps - step_where_duplicate_encountered)
