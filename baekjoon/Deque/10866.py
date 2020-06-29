import collections
import sys

deque = collections.deque()
n = int(sys.stdin.readline())


while n > 0:
    line = sys.stdin.readline().split()
    command = line[0]
    if command == 'push_front':
        deque.append(line[1])
    elif command == 'push_back':
        deque.appendleft(line[1])
    elif command == 'pop_front':
        print(-1 if len(deque) == 0 else deque.pop())
        pass
    elif command == 'pop_back':
        print(-1 if len(deque) == 0 else deque.popleft())
        pass
    elif command == 'size':
        print(len(deque))
        pass
    elif command == 'empty':
        print(1 if len(deque) == 0 else 0)
        pass
    elif command == 'front':
        print(-1 if len(deque) == 0 else deque[len(deque)- 1])
        pass
    elif command == 'back':
        print(-1 if len(deque) == 0 else deque[0])
        pass
    # print(deque)
    n -= 1
