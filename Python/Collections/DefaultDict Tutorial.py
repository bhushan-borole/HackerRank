# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import Counter
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(input())
d = Counter(A)

for _ in range(m):
    val = input()
    if val in d:
        l = [str(i+1) for i in range(len(A)) if A[i] == val]
    else:
        print("-1")
        continue
    print(' '.join(l))        