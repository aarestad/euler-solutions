from euler_functions import digit_permutations

n = 0

while True:
	n += 1
	if n % 10000 == 0: print n

	n6 = 6*n

	if len(str(n)) != len(str(n6)):
		n = 10 ** len(str(n)) - 1
		continue

	n2 = 2*n
	n3 = 3*n
	n4 = 4*n
	n5 = 5*n

	n_permutations = digit_permutations(n)

	if n in n_permutations and n2 in n_permutations and n3 in n_permutations and n4 in n_permutations and n5 in n_permutations and n6 in n_permutations:
		print n, n2, n3, n4, n5, n6
		break
