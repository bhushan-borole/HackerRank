# https://www.hackerrank.com/challenges/30-bitwise-and/problem

n = int(input())
for _ in range(n):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)
