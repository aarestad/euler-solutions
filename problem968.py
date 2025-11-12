from itertools import product

def p_seq(xab, xac, xad, xae, xbc, xbd, xbe, xcd, xce, xde):
  quintuple_sum = 0

  #max_exp = 1000000006
  max_a = max(xab, xac, xad, xae)
  max_b = max(xab, xbc, xbd, xbe)
  max_c = max(xac, xbc, xcd, xce)
  max_d = max(xad, xbd, xcd, xde)
  max_e = max(xae, xbe, xce, xde)

  for a, b, c, d, e in product(range(max_a+1), range(max_b+1), range(max_c+1), range(max_d+1), range(max_e+1)):
    if a+b <= xab and a+c <= xac and a+d <= xad and a+e <= xae and\
                      b+c <= xbc and b+d <= xbd and b+e <= xbe and\
                      c+d <= xcd and c+e <= xce and d+e <= xde:
      quintuple_sum += 2**a * 3**b * 5**c * 7**d * 11**e

  return quintuple_sum

def a_seq(n):
    if n == 0: return 1
    if n == 1: return 7
    return (7 * a_seq(n-1) + a_seq(n-2) ** 2) % 1000000007

def q_seq(n):
    return p_seq(
            a_seq(10*n  ), a_seq(10*n+1), a_seq(10*n+2),
            a_seq(10*n+3), a_seq(10*n+4), a_seq(10*n+5),
            a_seq(10*n+6), a_seq(10*n+7), a_seq(10*n+8), a_seq(10*n+9)
            )

if __name__ == "__main__":
  print(p_seq(2,2,2,2,2,2,2,2,2,2))
  print(p_seq(1,2,3,4,5,6,7,8,9,10))
  print(p_seq(10,9,8,7,6,5,4,3,2,1))

