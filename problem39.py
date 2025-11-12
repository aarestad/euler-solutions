p_values = {}
for a in range(1, 1001):
    for b in range(a, 1001 - a):
        for c in range(int((a**2 + b**2) ** 0.5), 1001 - b - a):
            if a**2 + b**2 != c**2:
                continue
            p = a + b + c
            print((a, b, c, p))
            if p in p_values:
                p_values[p] += 1
            else:
                p_values[p] = 1
max_v = 0
for k, v in list(p_values.items()):
    if v > max_v:
        max_v = v
print(max_v)


def is_bouncy(n):
    if n < 100:
        return False
    decreasing = None
    last_digit = None
    while n > 0:
        digit = n % 10
        n //= 10
        print(digit)
        print(("last_digit", last_digit))
        print(("decreasing", decreasing))
        if last_digit is not None:
            if decreasing is not None:
                if decreasing and digit > last_digit:
                    return True
                else:
                    print("still not increasing")
                if not decreasing and digit < last_digit:
                    return True
                else:
                    print("still not decreasing")
            else:
                if last_digit < digit:
                    print("decreasing")
                    decreasing = True
                elif last_digit > digit:
                    print("increasing")
                    decreasing = False
        last_digit = digit
    return False
