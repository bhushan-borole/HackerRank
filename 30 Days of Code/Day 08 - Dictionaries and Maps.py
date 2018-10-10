# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())
l = {}
for _ in range(n):
    name, number = map(str, input().split(' '))
    l[name] = number
while True:
    search = input()
    if search in l:
        print(search+'='+l[search])
    else:
        print('Not found')
    
