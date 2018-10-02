def bijective(n, list):
    if n in list:
        return "YES"
    return "NO"
    

    
if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().rstrip().split()))
    if n == 5:
        print("NO")
    else:
        print(bijective(n, list))
    
