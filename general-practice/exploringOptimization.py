# This is a program appearing on lecture: Introduction and Matrix Multiplication MIT 6.172
# I re-wrote it verify the speed of the program changing 'n' values.

# The objective of this program is to test optimization using python, showing Python isn't that fast at large scale
#       and rather is better to use a low level language, like C for example. This program should take around 6 hours as is, to complete.


import sys, random
from time import *

n = 4016

A = [[random.random()
      for row in range(n)]
     for col in range(n)]
B = [[random.random()
      for row in range(n)]
     for col in range(n)]
C = [[0 for row in range(n)]
     for col in range(n)]

start = time()
for i in range(n):
    for k in range(n):
        for j in range(n):
            C[i][j] += A[i][k] * B[k][j]

end = time()

#print('%0.6f' % (end - start))

print(end)