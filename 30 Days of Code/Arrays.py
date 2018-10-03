# https://www.hackerrank.com/challenges/30-arrays/problem

n = int(input())
array = list(map(str, input().split()))
array.reverse()
print(' '.join(array))
