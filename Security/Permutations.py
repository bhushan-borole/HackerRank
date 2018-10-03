# https://www.hackerrank.com/challenges/security-tutorial-permutations/problem

n = int(input())
l = list(map(int, input().split()))
#l1 = [0 for x in range(n)]
for i in range(n):
    print(l[l[i]-1])