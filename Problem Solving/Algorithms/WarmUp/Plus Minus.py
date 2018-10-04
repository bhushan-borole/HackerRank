# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    pos = [arr[i] for i in range(len(arr)) if(arr[i]>0)]
    neg = [arr[i] for i in range(len(arr)) if(arr[i]<0)]
    zero = [arr[i] for i in range(len(arr)) if(arr[i]==0)]
    print(len(pos)/len(arr))
    print(len(neg)/len(arr))
    print(len(zero)/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
