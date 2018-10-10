# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

'''
The problem is to find P(X <= 5). 
So we have to do this: P(1) + P(2) + P(3) + P(4) + P(5). 
This is a pretty bad thing to do since if it was say P(X <= 1000) a lot of calculations needed to be done.

Lets, approach the problem in a simpler way. 
First we find P(X > 5), i.e, a defect is found after the first 5 trials, i.e, the first 5 DID NOT have any defect. 
Which is basically (1 - p)^5. Now P(X <= 5) is the complement of P(X > 5) which leads us to (1 - P(X > 5)), this saves us a lot computations.
'''

a, b  = 1, 3
n = 5
p = a/b
q = 1-p
print(round(1-q**(n), 3))
