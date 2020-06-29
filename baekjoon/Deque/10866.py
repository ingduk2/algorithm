import collections
import sys

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.


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
