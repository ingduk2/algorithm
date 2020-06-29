import collections
import sys


def push(num):
    data_queue.appendleft(num)


def pop():
    if len(data_queue) == 0:
        return -1
    return data_queue.pop()


def size():
    return len(data_queue)


def empty():
    if len(data_queue) == 0:
        return 1
    return 0


def front():
    if len(data_queue) == 0:
        return -1
    return data_queue[len(data_queue)-1]


def back():
    if len(data_queue) == 0:
        return -1
    return data_queue[0]


data_queue = collections.deque()
n = int(sys.stdin.readline())
while n > 0:
    input = sys.stdin.readline().split()
    command = input[0]
    if command == 'push':
        push(input[1])
    elif command == 'pop':
        print(pop())
    elif command == 'size':
        print(size())
    elif command == 'empty':
        print(empty())
    elif command == 'front':
        print(front())
    elif command == 'back':
        print(back())
    n -= 1

