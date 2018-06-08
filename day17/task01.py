buffer = [0]
cursor = 0
step_size = 354

for value in [i + 1 for i in range(2017)]:
    cursor = ((cursor + step_size) % len(buffer)) + 1
    buffer = buffer[:cursor] + [value] + buffer[cursor:]

print(buffer[cursor + 1])
