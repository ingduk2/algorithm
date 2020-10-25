import heapq


def solution(operations):
    hq = []
    for o in operations:
        op, num = o.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(hq, num)
        elif op == 'D' and num == 1 and hq:
            max_n = max(hq)
            hq.remove(max_n)
        elif op == 'D' and num == -1 and hq:
            heapq.heappop(hq)

    if hq:
        return [max(hq), heapq.heappop(hq)]
    else:
        return [0, 0]

oprtarions = ["I 16","I 16","I 16","I 1", "D 1"]
print(solution(oprtarions))
print("==========================")
oprtarions = ["I 7","I 5","I -5","D -1"]
print(solution(oprtarions))
print("==========================")
oprtarions = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(oprtarions))
print("==========================")
oprtarions = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(oprtarions))
print("==========================")