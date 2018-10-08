# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

import math
l = float(input())
k = int(input())
print(math.exp(-l) * (l**k) / math.factorial(k))