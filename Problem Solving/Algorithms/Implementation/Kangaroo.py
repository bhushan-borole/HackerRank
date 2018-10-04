# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(l):
    x1 = l[0]
    v1 = l[1]
    x2 = l[2]
    v2 = l[3]
    if x1 != x2 and v1 == v2:
        print("NO")
    elif x1 == x2 and v1 == v2:
        print("YES")
    
    elif x1 == x2 and v1 > v2 :
        print("NO")
    
    elif x1 <= x2 and v1 <= v2 :
        print("NO")
    
    else :
        if (x2 - x1) % (v1 - v2) == 0 : 
            print("YES")
        
        else :
            print("NO")
        

if __name__ == '__main__':
    n = list(map(int, input().rstrip().split()))
    kangaroo(n)
