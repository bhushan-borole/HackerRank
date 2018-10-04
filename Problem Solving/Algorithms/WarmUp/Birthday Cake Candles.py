# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthday(arr):
    arr.sort()
    max = arr[len(arr)-1]
    list = [arr[i] for i in range(len(arr)) if(arr[i]==max)]
    print(len(list))
        
if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    birthday(arr)
