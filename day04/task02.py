def sort_letters(word):
    letter_list = list(word)
    letter_list.sort()
    return ''.join(letter_list)


def passphrase_is_valid(passphrase: str) -> bool:
    words = [sort_letters(word) for word in passphrase.split()]
    word_set = set(words)
    return len(words) == len(word_set)


def count_valid_in_input():
    valid_count = 0

    with open('input.txt') as file:
        for line in file:
            if passphrase_is_valid(line):
                valid_count += 1

    return valid_count


# print(count_valid_in_input())
