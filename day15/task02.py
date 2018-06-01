def aoc_generator(seed, factor, modulo_check, n):
    last_value = seed
    yield_count = 0
    while yield_count < n:
        last_value = (last_value * factor) % 2147483647

        if last_value % modulo_check == 0:
            yield last_value
            yield_count += 1


def low_16bit_match(a, b):
    # Find the lowest different bit, ensure it's higher than the 16th bit (from the right)
    xor = a ^ b
    return xor & -xor >= 65536


def judge_count(is_example, n):
    seed_a = 65 if is_example else 516
    seed_b = 8921 if is_example else 190

    gen_a = aoc_generator(seed_a, 16807, 4, n)
    gen_b = aoc_generator(seed_b, 48271, 8, n)

    matches_count = 0
    for a, b in zip(gen_a, gen_b):
        if low_16bit_match(a, b):
            matches_count += 1

    return matches_count


print(judge_count(False, 5_000_000))
