def floyd_cycle_detection(s):
	tortoise = 1
	hare = 2
	try:
	    while s[tortoise] != s[hare]:
	        tortoise += 1
	        hare += 2

	    mu = 0
	    tortoise = 0

	    while s[tortoise] != s[hare]:
	        tortoise += 1
	        hare += 1
	        mu += 1

	    lam = 1
	    hare = tortoise + 1

	    while s[tortoise] != s[hare]:
	        hare += 1
	        lam += 1

	    return lam, mu
	except IndexError:
		return 0, 0

def fibs():
  x0 = 1
  x1 = 2
  yield x0
  yield x1
  while True:
    new_fib = x0 + x1
    yield new_fib
    x0 = x1
    x1 = new_fib

def palindrome(n):
  s = str(n)
  return s == s[::-1]

def find_largest_palindrome():
  largest_palindrome = 0
  for x in range(100, 1000):
    for y in range(x, 1000):
      product = x * y
      if palindrome(product) and product > largest_palindrome:
        largest_palindrome = product
  return largest_palindrome

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f +=6
    return True

def nth_prime(n):
  if n == 1: return 2
  p = 3
  n -= 2
  while n > 0:
    p += 2
    while not is_prime(p): p += 2
    n -= 1
  return p

def triangle_numbers():
  t = 1
  i = 1
  while True:
    yield t
    i += 1
    t += i

def primes():
  yield 2
  p = 3
  while True:
    yield p
    p += 2
    while not is_prime(p): p += 2

# Euler 9
def find_triplet():
  for a in range(1, 1000):
    remaining_sum = 1000 - a
    for b in range(1, remaining_sum+1):
      c = 1000 - a - b
      if a ** 2 + b ** 2 == c ** 2:
        print a, b, c
        print a * b * c
        return

def factorize(n):
  factors = []
  for p in primes():
    if p*p > n: break
    i = 0
    while n % p == 0:
      n //= p
      i+=1
    if i > 0:
      factors.append((p, i));
  if n > 1: factors.append((n, 1))
  div = [1]
  for (p, r) in factors:
    div = [d * p**e for d in div for e in range(r + 1)]
  return div

def collatz_sequence(n):
  while n > 1:
    yield n
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1

def nCr(n,r):
  import math
  f = math.factorial
  return f(n) / f(r) / f(n-r)

def to_letters(n):
  words = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
  }
  descrip = ''
  if n == 1000:
    return 'onethousand'
  if n >= 100:
    times_100 = n / 100
    descrip += words[times_100]
    descrip += 'hundred' # so 'one hundred', 'two hundred', etc.
    n %= 100
    if n > 0:
      descrip += 'and'
    else:
      return descrip # exactly 'x hundred'
  if n <= 19:
    descrip += words[n] # up to 'nineteen'
  else:
    times_10 = n / 10
    descrip += words[times_10*10] # 'twenty', 'thirty,'' etc.
    n %= 10
    if n > 0: descrip += words[n] # 'one' thru 'nine'
  return descrip
