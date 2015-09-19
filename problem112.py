def is_bouncy(n):
  if n < 100: return False
  decreasing = None
  last_digit = None
  while n > 0:
    digit = n % 10
    n //= 10
    if last_digit is not None:
      if decreasing is not None:
        if decreasing and digit > last_digit:
          return True
        if not decreasing and digit < last_digit:
          return True
      else:
        if last_digit > digit:
          decreasing = True
        elif last_digit < digit:
          decreasing = False
    last_digit = digit
  return False
from fractions import Fraction
bouncy_numbers = 0
current_number = 0
target = Fraction(99, 100)

while True:
  current_number += 1
  if is_bouncy(current_number):
    bouncy_numbers += 1
  if Fraction(bouncy_numbers, current_number) == target:
    print(current_number)
    break