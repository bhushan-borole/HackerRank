if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l = sorted(set(arr))
    if len(l)==1:
        print(l[0])
    else:
        print(l[-2])