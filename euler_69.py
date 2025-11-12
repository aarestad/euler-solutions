from euler_functions import totient, primes
import itertools

best_ratio = 0
best_n = 0

primes_under_a_thousand = []

# we don't need many primes, but no need to regenerate them every time!
for p in primes():
    if p <= 1000:
        primes_under_a_thousand.append(p)
    else:
        break

for n in range(2, 1000001):
    if n % 100000 == 0:
        print(n)
    totient_n = totient(n, primes_under_a_thousand)
    ratio = n / totient_n
    if ratio > best_ratio:
        print("new best:", n, "totient:", totient_n, "ratio:", ratio)
        best_ratio = ratio
        best_n = n
