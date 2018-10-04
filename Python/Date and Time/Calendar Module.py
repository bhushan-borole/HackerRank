# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
MM, DD, YYYY = map(int, input().split())
array = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(array[calendar.weekday(YYYY, MM, DD)])