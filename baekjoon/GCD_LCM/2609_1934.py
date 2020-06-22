import sys


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def lcm(x, y, g):
    return int(g * (x/g) * (y/g))


t = int(input())
while t > 0:
    a, b = map(int, input().split())
    print(lcm(a, b, gcd(a, b)))
    t -= 1;


