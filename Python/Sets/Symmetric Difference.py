n = int(input())
s = set(map(int, input().rstrip().split()))
m = int(input())
s1 = set(map(int, input().rstrip().split()))

s2 = s.symmetric_difference(s1)

l = sorted(list(s2))
for x in l:
    print(x)