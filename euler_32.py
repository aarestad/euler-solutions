from euler_functions import is_pandigital_set, number_digits
from functools import reduce

pandigital_products = set()

for x in range(10000):
    limit = 5 - number_digits(x)

    for y in range(10 ** limit):
        product = x * y

        if number_digits(product) + number_digits(x) + number_digits(y) != 9:
            continue

        if is_pandigital_set(x, y, product):
            print("%s x %s = %s" % (x, y, product))
            pandigital_products.add(product)

print(pandigital_products)
print(reduce(lambda x, y: x + y, pandigital_products))
