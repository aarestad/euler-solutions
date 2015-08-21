from fractions import Fraction
import itertools
import sys

def convergent(continued_fraction):
	return Fraction(continued_fraction[0], 1) + convergent_fraction(continued_fraction[1:])

def convergent_fraction(cf):
	if len(cf) == 0:
		return 0

	return Fraction(1, cf[0] + convergent_fraction(cf[1:]))

def e_convergent():
	yield 2
	n = 0
	while True:
		n += 2
		yield 1
		yield n
		yield 1

accuracy = 100

one_hundredth_convergent = convergent(list(itertools.islice(e_convergent(), accuracy)))

numer = one_hundredth_convergent.numerator

numer_digit_sum = 0

while numer > 0:
	numer_digit_sum += numer % 10
	numer /= 10

print one_hundredth_convergent
print numer_digit_sum
