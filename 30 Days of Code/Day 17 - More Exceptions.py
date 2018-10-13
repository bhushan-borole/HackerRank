# https://www.hackerrank.com/challenges/30-more-exceptions/problem

#Write your code here
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        return n ** p