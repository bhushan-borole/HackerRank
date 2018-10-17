# https://www.hackerrank.com/challenges/30-sorting/problem

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0
for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps  += 1
    if numberOfSwaps == 0:
        break
print('Array is sorted in '+ str(numberOfSwaps) +' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))