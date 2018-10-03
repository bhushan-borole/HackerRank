# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = map(int,input().split())
x = list(map(int, input().strip().split(' ')))
w = list(map(int, input().strip().split(' ')))
sum_x = sum([a*b for a,b in zip(x,w)])
print(round((sum_x/sum(w)),1))
