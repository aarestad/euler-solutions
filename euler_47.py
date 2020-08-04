from euler_functions import prime_factors

n = 1

while True:
    if n % 1000 == 0: print(n)
    n += 1
    num_factors = len(prime_factors(n))
    if num_factors != 4: continue
    n += 1
    num_factors = len(prime_factors(n))
    if num_factors != 4: continue
    n += 1
    num_factors = len(prime_factors(n))
    if num_factors != 4: continue
    n += 1
    num_factors = len(prime_factors(n))
    if num_factors == 4: break

print(n - 3)
