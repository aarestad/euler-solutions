numeral_values = {
	'M': 1000,
	'D': 500,
	'C': 100,
	'L': 50,
	'X': 10,
	'V': 5,
	'I': 1
}

subtractive_prefix_values = {
	'I': {
		'V': 4,
		'X': 9
	},
	'X': {
		'L': 40,
		'C': 90
	},
	'C': {
		'D': 400,
		'M': 900
	}
}

def from_roman_numeral(rn):
	decimal_rep = 0

	i = 0
	while i < len(rn):
		current_char = rn[i]
		#print current_char

		if current_char in subtractive_prefix_values and i < len(rn)-1:
			next_char = rn[i+1]
			if next_char in subtractive_prefix_values[current_char]:
				#print "adding %s for %s" % (subtractive_prefix_values[current_char][next_char], rn[i:i+2])
				decimal_rep +=  subtractive_prefix_values[current_char][next_char]
				i += 2 # skip the next character
				continue

		#print "adding %s for %s" % (numeral_values[current_char], current_char)
		decimal_rep += numeral_values[current_char]
		i += 1

	return decimal_rep

to_roman_numeral_values = [
	(1000, 'M'),
	(900, 'DM'),
	(500, 'D'),
	(400, 'CD'),
	(100, 'C'),
	(90, 'XC'),
	(50, 'L'),
	(40, 'XL'),
	(10, 'X'),
	(9, 'IX'),
	(5, 'V'),
	(4, 'IV'),
	(1, 'I'),
]
def to_roman_numeral(n):
	roman_rep = ''
	while n > 0:
		for v in to_roman_numeral_values:
			if n >= v[0]:
				roman_rep += v[1]
				n -= v[0]
				break

	return roman_rep

with open('p089_roman.txt') as numeral_input:
	numerals = numeral_input.readlines()

savings = 0

for original_roman in numerals:
	original_roman = original_roman.rstrip()
	decimal_rep = from_roman_numeral(original_roman)
	best_roman_rep = to_roman_numeral(decimal_rep)
	print original_roman, best_roman_rep, decimal_rep
	savings += len(original_roman) - len(best_roman_rep)

print "savings: %s" % (savings,)
