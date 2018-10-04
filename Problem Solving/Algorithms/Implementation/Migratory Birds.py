# https://www.hackerrank.com/challenges/migratory-birds/problem

from collections import Counter

def countNumberOfBirds(a):
    d = Counter(a)
    l = [u for(u,v) in d.items() if d[u] == max(d.values())]
    print(min(l))

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    countNumberOfBirds(ar)