def refactored_non_optimized():
    h = 0

    b = 100 * 99 + 100000
    c = b + 17000

    while True:
        f = False
        d = 2
        while True:
            e = 2

            while True:
                if d * e == b:
                    f = True
                e += 1
                if e == b:
                    break

            d += 1
            if d == b:
                break

        if f:
            h += 1

        if b == c:
            return h

        b += 17


def optimized():
    h = 0
    for x in range(109900, 126900 + 1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break

    return h


print(optimized())
