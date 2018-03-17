valid_count = 0


def passphrase_is_valid(passphrase: str) -> bool:
    words = passphrase.split()
    word_set = set(words)
    return len(words) == len(word_set)


with open('input.txt') as file:
    for line in file:
        if passphrase_is_valid(line):
            valid_count += 1

print(passphrase_is_valid('aa bb cc dd ee'))
print(passphrase_is_valid('aa bb cc dd aa'))
print(passphrase_is_valid('aa bb cc dd aaa'))
print(valid_count)

