def square_of_digits(n):
	sum_of_squares = 0

	while n > 0:
		sum_of_squares += (n % 10) ** 2
		n /= 10

	return sum_of_squares

numbers_that_end_up_at_89 = 0

largest_loop = 0

for x in range(1, 10000000):
	original_x = x
	loop_size = 0

	while x != 1 and x != 89:
		x = square_of_digits(x)
		loop_size += 1

	if x == 89:
		numbers_that_end_up_at_89 += 1

	if loop_size > largest_loop:
		print("loop size %s for starting value %s" % (loop_size, original_x))
		largest_loop = loop_size

print(numbers_that_end_up_at_89)
