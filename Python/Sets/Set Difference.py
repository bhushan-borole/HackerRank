n = int(input())
s = set(map(int, input().rstrip().split()))
n1 = int(input())
s1 = set(map(int, input().rstrip().split()))

print(len(s.difference(s1)))