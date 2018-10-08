# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math
mean, std = 70, 10
def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))    

# Greater than 80
print(round(100 *(1 - cdf(80)), 2))
# Greater than equal to 60
print(round(100 * (1 - cdf(60)), 2))
# Less than 60
print(round(100 * cdf(60), 2))
