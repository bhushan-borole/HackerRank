import math
n = int(input())
x = [int(item) for item in input().split()]
u = float(sum(x)/n)

E = [(x[i]-u)**2 for i in range(n)]

print(math.sqrt(sum(E)/n))
