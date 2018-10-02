n = int(input())

for _ in range(n):
    m = int(input())
    s = set(map(int, input().rstrip().split()))
    m1 = int(input())
    s1 = set(map(int, input().rstrip().split()))
    print(s.issubset(s1))
    
