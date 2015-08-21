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

def to_roman_numeral(n):
	roman_rep = ''
	while n > 0:
		if n >= 1000:
			roman_rep += 'M'
			n -= 1000
		elif n >= 900:
			roman_rep += 'DM'
			n -= 900
		elif n >= 500:
			roman_rep += 'D'
			n -= 500
		elif n >= 400:
			roman_rep += 'CD'
			n -= 400
		elif n >= 100:
			roman_rep += 'C'
			n -= 100
		elif n >= 90:
			roman_rep += 'XC'
			n -= 90
		elif n >= 50:
			roman_rep += 'L'
			n -= 50
		elif n >= 40:
			roman_rep += 'XL'
			n -= 40
		elif n >= 10:
			roman_rep += 'X'
			n -= 10
		elif n >= 9:
			roman_rep += 'IX'
			n -= 9
		elif n >= 5:
			roman_rep += 'V'
			n -= 5
		elif n >= 4:
			roman_rep += 'IV'
			n -= 4
		elif n >= 1:
			roman_rep += 'I'
			n -= 1
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
