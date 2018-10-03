# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

#Without numpy
def median(nums):
    if len(nums)%2 == 0:
        return round(sum(nums[len(nums)//2-1:len(nums)//2+1])/2)
    else:
        return nums[len(nums)//2]

def quartiles(N,nums):
    Q1 = median(nums[:len(nums)//2])
    Q2 = median(nums)
    if N%2 == 0:
        Q3 = median(nums[len(nums)//2:])
    else:
        Q3 = median(nums[len(nums)//2+1:])
    return Q1,Q2,Q3

N = int(input())
nums = [int(num) for num in input().split()]
freq = [int(freqs) for freqs in input().split()]
numbers = []
for i in range(len(nums)):
    numbers.append([nums[i]]*freq[i])
numbers = sorted([item for sublist in numbers for item in sublist])
Q1,Q2,Q3 = quartiles(N,numbers)
print(float(Q3-Q1))


#With numpy
import numpy as np

N = int(input())
nums = [int(num) for num in input().split()]
freq = [int(freqs) for freqs in input().split()]
numbers = []
for i in range(len(nums)):
    numbers.append([nums[i]]*freq[i])
numbers = sorted([item for sublist in numbers for item in sublist])

Q1 = np.median(numbers[:len(numbers)//2])
Q2 = np.median(numbers)
if len(numbers)%2 == 0:
    Q3 = np.median(numbers[len(numbers)//2:])
else:
    Q3 = np.median(numbers[len(numbers)//2+1:])

print(float(Q3-Q1))
