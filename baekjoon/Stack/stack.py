# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys


def push(num):
    stack.append(num)


def top():
    if len(stack) == 0:
        return -1
    return stack[len(stack)-1]


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

stack = []
n = int(sys.stdin.readline())
while n > 0:
    command_str = sys.stdin.readline().split()
    if command_str[0] == 'push':
        push(int(command_str[1]))
    elif command_str[0] == 'pop':
        print(pop())
    elif command_str[0] == 'size':
        print(size())
    elif command_str[0] == 'empty':
        print(empty())
    elif command_str[0] == 'top':
        print(top())
    n -= 1

