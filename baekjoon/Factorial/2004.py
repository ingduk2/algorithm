import sys


def calc(mul, num):
    cnt = 0
    tmp_mul = mul
    while num >= tmp_mul:
        cnt += num // tmp_mul
        tmp_mul *= mul
    return cnt


n, m = map(int, sys.stdin.readline().split())
print(min(calc(5, n) - calc(5, m) - calc(5, n-m),
    calc(2, n) - calc(2, m) - calc(2, n-m)))






