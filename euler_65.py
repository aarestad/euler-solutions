from euler_functions import convergent
import itertools

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
