# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

#basic logic of this solution is ignore everything else and just concentrate on the index of 'MARKS'

from collections import namedtuple
n = int(input())
marks = input().split().index("MARKS")
tot = 0
for _ in range(n):
    tot += int(input().split()[marks])
print(float(tot/n))