
from euler_functions import *
import math

def are_permutations(m, n):
	if num_digits(m) != number_digits(n): return False

	m_digits = []
	n_digits = []

	while m > 0:
		m_digits.append(m % 10)
		m //= 10

	while n > 0:
		n_digits.append(n % 10)
		n //= 10

	m_digits.sort()
	n_digits.sort()

	for i in range(len(m_digits)):
		if m_digits[i] != n_digits[i]:
			return False

	return True

if __name__ == '__main__':
	possible_prime_factors = []

	for p in primes():
		if p > math.sqrt(10 ** 7): break
		possible_prime_factors.append(p)

	best_ratio = 1000000

	for n in range(2, 10 ** 7):
		if n % 10000 == 0: print(n)
		n_totient = totient(n, possible_prime_factors)
		if are_permutations(n, n_totient):
			ratio = n / n_totient
			if ratio < best_ratio:
				print("new best n:", n, "totient:", n_totient, "ratio:", ratio)
				best_ratio = ratio
