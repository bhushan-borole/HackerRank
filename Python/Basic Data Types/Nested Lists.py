n = int(input())
l = []
name = []
grade = []
for _ in range(n):
    name1 = input(); name.append(name1)
    grade1 = float(input()); grade.append(grade1)
    l.append([name1, grade1])
    
secondLowest = sorted(set(grade))[1]
secondLowestNames = []
for i in range(n):
    if secondLowest == l[i][1]:
        secondLowestNames.append(l[i][0])

for x in sorted(secondLowestNames):
    print(x)s