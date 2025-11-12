#!/usr/bin/env python
# coding=utf8


def floyd(s):
    # Main phase of algorithm: finding a repetition x_i = x_2i
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = 0
    hare = 1
    while s[tortoise] != s[hare]:
        tortoise += 1
        hare += 2

        if hare >= len(s):
            return 0, 0

    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in circle one step at a time,
    # and tortoise (reset to x0) moving towards the circle, will
    # intersect at the beginning of the circle. Because the
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.
    mu = 0
    tortoise = 0
    while s[tortoise] != s[hare]:
        tortoise += 1
        hare += 1  # Hare and tortoise move at same speed
        mu += 1

    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = tortoise
    while s[tortoise] != s[hare]:
        hare += 1
        lam += 1

    return lam, mu


longest_lambda = 0

for d in range(2, 1000):
    recip = "{0:.100f}".format(1.0 / d)
    lam = floyd(recip)[0]
    if lam > longest_lambda:
        longest_lambda = lam
        print(d, recip, longest_lambda)
