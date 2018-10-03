# https://www.hackerrank.com/challenges/security-involution/problem

n = int(input())
l = list(map(int, input().split()))
bool = False
for i in range(n):
    if l[l[i]-1] == i+1:
        bool = True
    else:
        bool = False
        break
if bool:
    print("YES")
else:
    print("NO")
        
