from decimal import *
import euler_functions

from decimal import *

# hat tip to http://ubuntuforums.org/showthread.php?t=865953

def Floyd(x):  # Using Floyd's cycle detection algorithm
   # Only proceed if there are enough decimal numbers to actually find a large cycle
   if len(x) > 100:
      # The main phase of the algorithm, finding a repetition x_nu = x_2nu
      # The hare moves twice as quickly as the turtle
      turtle, hare = 1, 2
      while x[turtle] != x[hare]:
         turtle = turtle + 1
         hare = hare + 2

      # Find the position of the first repetition of length nu
      # The hare and turtle move at the same speeds
      mu = 0
      turtle, hare = 0, turtle
      while x[turtle] != x[hare]:
         turtle = turtle + 1
         hare = hare + 1
         mu = mu + 1

      # Find the length of the shortest cycle starting from x_mu
      # The hare moves while the turtle stays still
      lam = 1
      hare = turtle + 1
      while x[turtle] != x[hare]:
        hare = hare + 1
        lam += 1

      # Verify that the obtained mu and lambda does indeed describe a cycle
      if verifyCycle(x, mu, lam) == True:
         return mu, lam
      else:
         return -1, -1
   else:
      return 0, 0


def getRecurringCycle(x):
   # Only proceed if there are enough decimal numbers to actually find a large cycle
   maxLength = len(x)
   if maxLength > 100:
      mu, lam = Floyd(x)   # Try finding a cycle using Floyd's algorithm
      if (mu != -1) and (lam != -1):
         return mu, lam
      else:                # Otherwise try a brute force approach
         mu = 0
         lam = 1
         sequenceFound = False
         while not sequenceFound:
            while (mu + lam < maxLength) and x[mu] != x[mu + lam]:
               lam += 1
            if verifyCycle(x, mu, lam) == True:
               sequenceFound = True
            elif lam < maxLength:
               lam += 1
            else:
               mu += 1
               lam = 1

         return mu, lam
   else:
      return 0, 0


def verifyCycle(x, mu, lam):
   # Verify that the calculated cycle is indeed correct
   # This algorithm is not fool proof
   if (2 * lam + mu) < len(x):
      for j in range(len(x) / lam):
         for i in range(lam):
            if x[mu + i] != x[mu + lam + i]:
               return False
      if lam < 10:   # As a precaution...
         for i in range(10):  # 10 is arbitrary...
            if x[mu + i] != x[mu + i + 1]:
               return False
      return True
   else:
      return False


def printResult(a, d, mu, lam):
   # Print the result on a form that's easily readable
   if (lam > 0) or (mu > 0):
      number = '1/' + str(d) + ' = 0.'
      for i in range(2, mu + 2):
         number = number + a[i]
      number = number + '('
      for i in range(mu + 2, mu + lam + 2):
         number = number + a[i]
      number = number + ')' + ' lambda = ' + str(lam) + ' mu = ' + str(mu)
   elif (lam == -1) or (mu == -1):
      number = '1/' + str(d) + ' could not be calculated.'
   else:
      number = '1/' + str(d) + ' = ' + str(Decimal(1) / Decimal(d))
   print number


if __name__ == "__main__":
   getcontext().prec = 2000
   longest_lambda = 0

   for d in range(2, 1000):
      a = str(Decimal(1) / Decimal(d))
      x = []
      for i in range(2, len(a)):
         x.append(int(a[i]))
      mu, lam = getRecurringCycle(x)

      if lam > longest_lambda:
		  longest_lambda = lam
		  printResult(a, d, mu, lam)
