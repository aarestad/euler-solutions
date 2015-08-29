from fractions import Fraction
from euler_functions import gcd

fractions_below_limit = []

seen_fractions = set()

limit = Fraction(3, 7)

def add_fractions_for(d):
	for n in range(1, d):
		if gcd(n, d) > 1: continue
		f = Fraction(n, d)
		if f > limit: return
		if f in seen_fractions : continue
		seen_fractions.add(f)
		fractions_below_limit.append(f)

for d in range(1, 1000001):
	if d % 100 == 0: print d
	add_fractions_for(d)


sort(fractions_below_limit)

print fractions_below_limit[-2]
