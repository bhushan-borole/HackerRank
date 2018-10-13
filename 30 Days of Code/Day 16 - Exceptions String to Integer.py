# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

#!/bin/python3
S = input().strip()
try:
    x = int(S)
    print(x)
except:
    print("Bad String")