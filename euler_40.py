champernowne = ""

for n in range(1, 1000001):
	champernowne += str(n)

print int(champernowne[0]) * int(champernowne[9]) * int(champernowne[99]) * \
	  int(champernowne[999]) * int(champernowne[9999]) * int(champernowne[99999]) * \
	  int(champernowne[999999])
