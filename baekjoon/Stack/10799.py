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


line = sys.stdin.readline().split()[0]
stack = []
count = 0
for i in range(len(line)):
    if line[i] == '(':
        push(i)
    else:
        index = pop()
        if i - index == 1:
            #print(len(stack))
            count += len(stack)
        else:
            #print(1)
            count += 1
    #print(stack)
print(count)






