# https://www.hackerrank.com/challenges/collections-counter/submissions/code/85894336

from collections import Counter
n = int(input())
cost = 0
l = list(map(int, input().rstrip().split(" ")))
x = int(input())
for _ in range(x):
    size, price = map(int, input().split())
    if(l.count(size)>0):
        cost += price
        l.remove(size)
print(cost)        
        
    
    
    

    
