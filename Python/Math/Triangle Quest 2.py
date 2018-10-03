# https://www.hackerrank.com/challenges/triangle-quest-2/problem

#just use math's trick:
#pow(1,2)=1 pow(11,2)=121 pow(111,2)=12321 pow(1111,2)=1234321 and so on code will be :: 
for i in range(1,int(input())+1): 
    print (((10**i - 1)//9)**2)