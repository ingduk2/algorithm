import sys


def prime_2(x):
    if x < 2:
        return False
    for i in range(2, x // 2 + 1, 1):
        # print(i)
        if x % i == 0:
            return False
    return True


n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if prime_2(i):
        count += 1
print(count)
