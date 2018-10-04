# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diag1 = [arr[i][j] for i in range(len(arr)) for j in range(len(arr)) if(i==j)]
    #print(diag1)
    sum1,sum2 = 0,0
    for x in diag1:
        sum1 = sum1 + x
    diag2 = [arr[i][j] for i in range(len(arr)) for j in range(len(arr)) if (i+j==len(arr)-1)]
    #print(diag2)
    for y in diag2:
        sum2 = sum2 + y
    return abs(sum1-sum2)    

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
        
