import sys


def prime_1(x):
    if x < 2:
        return False
    for i in range(2, x, 1):
        #print(i)
        if x % i == 0:
            return False
    return True


def prime_2(x):
    if x < 2:
        return False
    for i in range(2, x // 2 + 1, 1):
        #print(i)
        if x % i == 0:
            return False
    return True


def prime_3(x):
    if x < 2:
        return False
    for i in range(2, x//2, 1):
        #print(i)
        if x % i == 0:
            return False
    return True

print(prime_1(97))
print(prime_2(97))

for i in range(1, 10, 1):
    print(i)