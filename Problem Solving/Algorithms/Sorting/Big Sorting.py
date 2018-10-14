# https://www.hackerrank.com/challenges/big-sorting/problem

def bigSorting(unsorted):
    unsorted.sort(key=int)
    for s in unsorted:
        print(s)

n = int(input())
l = []
for _ in range(n):
    l.append(input())
bigSorting(l)