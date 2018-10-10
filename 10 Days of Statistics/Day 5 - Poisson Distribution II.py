# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

# Var(X) = E(X) = λ 
# E(X²) = λ + λ²

averageX, averageY = [float(num) for num in input().split(" ")]

X = 160 + 40*(averageX + averageX**2)
Y = 128 + 40*(averageY + averageY**2)

print(round(X, 3))
print(round(Y, 3))