from math import factorial

def sum_of_factorials_of_digits(n):
	the_sum = 0
	while n > 0:
		the_sum += factorial(n % 10)
		n /= 10
	return the_sum

long_chains = 0

seen_numbers = set()

for n in range(1, 1000000):
	if n % 10000 == 0: print(n)
	current_loop = n

	seen_numbers.clear()

	while True:
		seen_numbers.add(current_loop)
		next_loop = sum_of_factorials_of_digits(current_loop)
		if next_loop in seen_numbers: break
		current_loop = next_loop

	if len(seen_numbers) == 60:
		long_chains += 1

print(long_chains, "total chains of 60")
