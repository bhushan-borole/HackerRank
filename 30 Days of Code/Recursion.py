# https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(int(input())))