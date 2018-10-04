# https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def min_max(arr):
    arr.sort()
    sum1,sum2 = 0,0
    for i in range(len(arr)-1):
        sum1 = sum1 + arr[i]
    for i in range(1,len(arr)):
        sum2 = sum2 + arr[i]
    print(sum1,end=" ")
    print(sum2)
        
if __name__ == '__main__':    
    arr = list(map(int, input().rstrip().split()))
    min_max(arr)

