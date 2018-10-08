# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

import math
def cmf(mean, std):
    return 0.5 * (1 + math.erf((250-mean)/(std*(2**0.5))))
print(round(cmf(2.4*100, 2*10), 4))
