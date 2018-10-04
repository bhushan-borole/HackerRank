# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a1 = [i+a for i in apples]
    o1 = [i+b for i in oranges]
    count1 = len([i for i in a1 if i>=s and i<=t])
    count2 = len([i for i in o1 if i>=s and i<=t])
    print(count1)
    print(count2)
    
    