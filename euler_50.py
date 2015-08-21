from euler_functions import primes, is_prime

primes_below_a_million = []

for p in primes():
	if p < 1000000:
		primes_below_a_million.append(p)
	else:
		break

most_primes = 0

for i in range(len(primes_below_a_million)):
	num_primes = 0
	prime_list = []
	while i < len(primes_below_a_million):
		prime_list.append(primes_below_a_million[i])
		prime_sum = reduce(lambda x, y: x+y, prime_list)
		if prime_sum >= 1000000: break
		num_primes += 1
		i += 1

		if is_prime(prime_sum) and num_primes > most_primes:
			print prime_sum
			print prime_list
			most_primes = num_primes
