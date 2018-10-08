# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#You dont need a binary conversion for this problem.

num = int(input())
result = 0
maximum = 0
while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result
    else:
        result = 0
    num //= 2
print(maximum)