cursor = 0
step_size = 354
last_value_at_1 = -1

for value in [i + 1 for i in range(50_000_000)]:
    cursor = ((cursor + step_size) % value) + 1
    if cursor == 1:
        last_value_at_1 = value

print(last_value_at_1)
