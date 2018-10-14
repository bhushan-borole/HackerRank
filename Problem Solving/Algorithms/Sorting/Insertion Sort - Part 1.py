# https://www.hackerrank.com/challenges/insertionsort1/problem

n = int(input())
l = list(map(int, input().rstrip().split()))
X = l[-1]
check = False
for i in range(len(l)-2, -2, -1):
    if i != -1:
        if X < l[i]:
            l[i+1] = l[i]
        else:
            l[i+1] = X
            check = True
    else:
        l[0] = X
    
    print(' '.join([str(x) for x in l]))
    if check:
          break
