A, n = set(input().split()), int(input())
flag = True
for i in range(n):
    newSet = set(input().split())
    if not (A > newSet):
        flag = False
        break
print(flag)