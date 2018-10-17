# https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(' '.join([str(x) for x in arr]))

n = int(input())
arr = list(map(int, input().rstrip().split()))
insertionSort2(arr)
    
