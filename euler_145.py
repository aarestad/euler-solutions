def all_digits_odd(n):
    if n == 0: return False
    while n > 0:
        if (n % 10) % 2 == 0: return False
        n //= 10
    return True

def reverse_digits_2(n):
    reversed_n = 0
    exp = len(str(n)) - 1
    while exp >= 0:
        reversed_n += (n % 10) * (10 ** exp)
        n //= 10
        exp -= 1
    return reversed_n

from multiprocessing import Process

def count_reversibles(ns):
    for n in ns:
        if n % 1000000 == 0: print(n)
        if n not in reversible_nums and n % 10 != 0:
            reversed_n = reverse_digits_2(n)

            if all_digits_odd(n + reversed_n):
                reversible_nums[n] = True
                reversible_nums[reversed_n] = True

threads = []
reversible_nums = {}

for n in range(8):
    threads.append(Process(target=count_reversibles, args=(list(range(125000000*n, 125000000*(n+1))),)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print((len(list(reversible_nums.keys()))))
