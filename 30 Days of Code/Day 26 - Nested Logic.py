# https://www.hackerrank.com/challenges/30-nested-logic/problem

ad, am, ay = map(int, input().split(' '))
ed, em, ey = map(int, input().split(' '))

if [ad, am, ay] == [ed, em, ey]:
    print(0)
elif [am, ay] == [em, ey]:
    print(15*(ad - ed))
elif ay == ey:
    if ad <= ed and am <= em:
        print(0)
    else:
        print(500*(am - em))
elif ay > ey:
    print(10000)
else:
    print(0)
    
    