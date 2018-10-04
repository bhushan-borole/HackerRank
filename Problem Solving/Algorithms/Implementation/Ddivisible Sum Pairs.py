# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n ,k ,a):
    count = 0
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if((a[i]+a[j])% k == 0):
                count += 1
    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))
    print(divisibleSumPairs(n, k, ar))



