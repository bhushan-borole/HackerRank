# https://www.hackerrank.com/challenges/find-angle/problem

import math
AB = float(input())
BC = float(input())

print(str(round(math.degrees(math.atan2(AB, BC))))+'°')