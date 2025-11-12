# 1_2_3_4_5_6_7_8_9_0


def is_magic_number(n):
    if n % 10 != 0:
        return False
    n //= 100
    if n % 10 != 9:
        return False
    n //= 100
    if n % 10 != 8:
        return False
    n //= 100
    if n % 10 != 7:
        return False
    n //= 100
    if n % 10 != 6:
        return False
    n //= 100
    if n % 10 != 5:
        return False
    n //= 100
    if n % 10 != 4:
        return False
    n //= 100
    if n % 10 != 3:
        return False
    n //= 100
    if n % 10 != 2:
        return False
    n //= 100
    return n % 10 == 1


for n in range(1010101010, 1414213563):
    if n % 1000000 == 0:
        print(n)
    if is_magic_number(n**2):
        print("FOUND IT")
        print(n)
        print("FOUND IT")
        break
