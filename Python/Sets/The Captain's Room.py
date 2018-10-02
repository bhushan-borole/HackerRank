from collections import Counter
n = int(input())
l = list(map(int, input().rstrip().split()))
d = Counter(l)

for k,v in d.items():
    if v != n:
        print(k)
