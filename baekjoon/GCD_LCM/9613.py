import sys


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


t = int(input())
while t > 0:
    numbers = map(int, input().split())
    n = next(numbers)
    listNum = list(numbers)
    sum= 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += gcd(listNum[i], listNum[j])
    print(sum)
    t -= 1
