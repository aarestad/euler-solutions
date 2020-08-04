from euler_functions import is_pandigital_set, number_digits

for x in range(9123, 9876): # much smaller range: http://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/
	products = []

	n = 1

	num_digits_in_products = 0

	while num_digits_in_products < 9:
		products.append(x * n)
		n += 1

		num_digits_in_products = 0
		for p in products:
			num_digits_in_products += number_digits(p)

		if is_pandigital_set(*products):
			print(products)
			break
