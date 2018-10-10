# https://www.hackerrank.com/challenges/30-review-loop/problem

n = int(input())
for i in range(n):
    l = list(input())
    print(''.join(l[0::2]),end=' ')
    print(''.join(l[1::2]))
    