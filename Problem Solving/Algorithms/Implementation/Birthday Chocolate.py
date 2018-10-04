# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s,d,m):
    cnt = 0
    if len(s) == 1:
        if(d == s[0]):
            return 1
    else:    
        for i in range(0,len(s)-m+1):
            count = 0
            for j in range(i,i+m):
                count = count + s[j]
            if count ==  d:
                cnt += 1
    return cnt
                
if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))
    d = x[0]
    m = x[1]
    print(birthday(s,d,m))
