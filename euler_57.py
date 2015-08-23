from euler_functions import convergent
import sys

sys.setrecursionlimit(2000)

numerator_has_more_digits = 0

for n in range(1, 1001):
	if n % 100 == 0: print n
	partial_sqrt2_convergent = convergent([1] + ([2] * n))
	if len(str(partial_sqrt2_convergent.numerator)) > len(str(partial_sqrt2_convergent.denominator)):
		numerator_has_more_digits += 1

print numerator_has_more_digits
