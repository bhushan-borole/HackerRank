# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

n = int(input())
scores = list(map(int, input().rstrip().split()))
maxScore = minScore = scores[0]
maxCount = minCount = 0
for i in range(n):
    if scores[i] < minScore:
        minScore = scores[i]
        minCount += 1
    if scores[i] > maxScore:
        maxScore = scores[i]
        maxCount += 1
print(maxCount, minCount)
        

