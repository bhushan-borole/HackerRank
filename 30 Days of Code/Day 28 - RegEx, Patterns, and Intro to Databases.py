# https://www.hackerrank.com/challenges/30-regex-patterns/problem

n = int(input())
names = []
for i in range(n):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    if '@gmail.com' in emailID:
        names.append(firstName)
print('\n'.join(sorted(names)))
        
