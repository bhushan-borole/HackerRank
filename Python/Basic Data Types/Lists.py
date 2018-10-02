if __name__ == '__main__':
    l = []
    n = int(input())
    for _ in range(n):
        operation = input().rstrip().split(" ")
        op = operation[0]
        if op == 'insert':
            l.insert(int(operation[1]), int(operation[2]))
        if op == 'print':
            print(l)
        if op == 'remove':
            l.remove(int(operation[1]))
        if op == 'append':
            l.append(int(operation[1]))
        if op == 'sort':
            l.sort()
        if op == 'pop':
            l.pop()
        if op == 'reverse':
            l.reverse()
        
        
