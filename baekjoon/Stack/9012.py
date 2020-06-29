import sys


def push(num):
    stack.append(num)


def top():
    if len(stack) == 0:
        return -1
    return stack[len(stack) - 1]


def pop():
    if len(stack) == 0:
        return -1

    num = stack[len(stack) - 1]
    del stack[len(stack) - 1]
    return num


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0


n = int(sys.stdin.readline())
while n > 0:
    string = sys.stdin.readline().split()[0]
    stack = []
    result = True
    for i in range(len(string)):
        if string[i] == '(':
            push(string[i])
        else:
            if pop() == '(':
                pass
            else:
                result = False
    if len(stack) == 0 and result == True:
        print("YES")
    else:
        print("NO")

    n -= 1
