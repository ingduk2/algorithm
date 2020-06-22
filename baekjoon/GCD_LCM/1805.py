import sys


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


a, b = map(int, input().split())
num = gcd(a, b)
for i in range(num):
    print("1", end='')
print()

