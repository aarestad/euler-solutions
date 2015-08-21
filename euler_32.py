all_digits = {n for n in range(1, 10)}

def is_pandigital_set(*nums):
	digits = all_digits.copy()
	for n in nums:
		while n > 0:
			d = n % 10
			n /= 10
			if d not in digits: return False
			try:
				digits.remove(d)
			except KeyError:
				return False
	return len(digits) == 0

def number_digits(n):
	if n == 0: return 1

	digits = 0

	while n > 0:
		n /= 10
		digits += 1

	return digits

pandigital_products = set()

for x in range(10000):
	limit = 5 - number_digits(x)

	for y in range(10 ** limit):
		product = x * y
		if number_digits(product) + number_digits(x) + number_digits(y) != 9: continue
		if is_pandigital_set(x, y, product):
			print "%s x %s = %s" % (x, y, product)
			pandigital_products.add(product)

print reduce(lambda x, y: x + y, pandigital_products)
