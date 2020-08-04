from fractions import Fraction

for x in range(10, 100):
	for y in range(10, 100):
		if x != y and x % 10 == y / 10 and y % 10 != 0 and Fraction(x, y) == Fraction(x/10, y % 10):
			print(x, y, Fraction(x, y))
