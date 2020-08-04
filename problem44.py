def pentagonals():
  n = 1
  while True:
    yield n
    n = (n * (3*n-1))/2

prev_pentagonals = []

for n in pentagonals():
  if len(prev_pentagonals) > 0:
    for p in prev_pentagonals:
      pass

  prev_pentagonals.append(n)

p_values = {}
for a in range(1, 1001):
  for b in range(a, 1001-a):
    for c in range(a**2 + b**2, 1001-b-a):
      print(("trying", a, b, c))
      if a**2 + b**2 != c**2: continue
      p = a + b + c
      print((a, b, c, p))
      if p in p_values:
        p_values[p] += 1
      else:
        p_values[p] = 1