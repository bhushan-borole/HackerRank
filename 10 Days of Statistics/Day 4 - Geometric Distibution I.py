# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

a, b  = 1, 3
n = 5
p = a/b
q = 1-p
print(round((q**(n-1))*p, 3))
