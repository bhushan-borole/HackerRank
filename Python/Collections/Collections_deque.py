# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque


d = deque()
n = int(input())

for i in range(n):
    exp = input().split(' ')
    f = exp[0]

    if f == 'append':
        d.append(exp[1])

    elif f == 'appendleft':
        d.appendleft(exp[1])

    elif f == 'pop':
        d.pop()

    elif f == 'popleft':
        d.popleft()

print(' '.join([de for de in d])) 
