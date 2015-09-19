

for n in range(2, 1000):
  print(n, "has a cycle of length", find_cycle_len(str(1/n)[2:]))