n = int(input())
s = set(map(int, input().split())) 
n1 = int(input())
for _ in range(n1):
    op = input().split(' ')
    if op[0] == 'intersection_update':
        s1 = set(map(int, input().split()))
        s.intersection_update(s1)
            
    if op[0] == 'update':
        s1 = set(map(int, input().split()))
        s.update(s1)
    if op[0] == 'symmetric_difference_update':
        s1 = set(map(int, input().split()))
        s.symmetric_difference_update(s1)
    if op[0] == 'difference_update':
        s1 = set(map(int, input().split()))
        s.difference_update(s1)

print(sum(s))

