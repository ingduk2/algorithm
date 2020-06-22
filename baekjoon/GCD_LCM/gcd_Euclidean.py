import sys


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


print(gcd(10, 2))
