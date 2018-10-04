# https://www.hackerrank.com/challenges/exceptions/problem

n = int(input())
for i in range(n):
    a,b = input().split()
    try :
        div = int(a)//int(b)
        print(int(div))
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print ("Error Code:",e)