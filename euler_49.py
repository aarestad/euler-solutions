from euler_functions import is_prime, digit_permutations

for n in range(1000, 10000):
	if not is_prime(n): continue

	prime_perms = [n]

	for p in digit_permutations(n):
		if p != n and p > 1000 and is_prime(p) and p not in prime_perms:
			prime_perms.append(p)

	if len(prime_perms) >= 3:
		prime_perms.sort()

		for i in range(len(prime_perms) - 2):
			for j in range(i+1, len(prime_perms) - 1):
				for k in range(j+1, len(prime_perms)):
					if prime_perms[k] - prime_perms[j] ==  prime_perms[j] - prime_perms[i]:
						print prime_perms[i], prime_perms[j], prime_perms[k]
