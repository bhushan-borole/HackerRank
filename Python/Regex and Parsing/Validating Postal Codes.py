# https://www.hackerrank.com/challenges/validating-postalcode/problem

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

'''
the first parentheses-delimited expression inside of the regex. 
It will return the number of alternate matching pattern which should be at max 1. 
SO the condition is of <2. re.findall function will take a pattern and a string. 
So we matches the digit \d. (?=...) Matches if ... matches next, but doesn’t consume any of the string. T
his is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.
'''