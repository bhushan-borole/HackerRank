# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
d = OrderedDict()
n = int(input())

for _ in range(n):
    name, xyz, price = input().rpartition(' ')
    d[name] = d.get(name, 0) + int(price) 
    #d.get(name, 0) This is the Value to be returned in case key does not exist.
    
for k, v in d.items():
    print(k,v)