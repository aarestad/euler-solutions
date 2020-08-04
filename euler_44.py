import itertools
import math


def pentagonal_numbers():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1


def is_pentagonal(n):
    x = (math.sqrt(24 * n + 1) + 1) / 6  # inverse function: https://en.wikipedia.org/wiki/Pentagonal_number
    return x == int(x)


pentagonals = list(itertools.islice(pentagonal_numbers(), 10000))

best_difference = 10000000000000

n = 0
for p1 in pentagonals:
    n += 1
    for p2 in pentagonals[n:]:
        if is_pentagonal(p1 + p2) and is_pentagonal(abs(p1 - p2)) and best_difference > abs(p1 - p2):
            best_difference = abs(p1 - p2)
            print("%s %s new best difference: %s" % (p1, p2, best_difference,))
            break  # no sense in going higher
