import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque([])
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))

    print(days)

    point = 0
    cnt = 1
    while days:
        # print(days)
        if point == 0:
            point = days.popleft()

        if not days:
            break

        if point >= days[0]:
            days.popleft()
            cnt += 1
        else:
            point = 0
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
print("=======")

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
# [5, 10, 1, 1, 20, 1]
#  1   (1 1 1 )  2
print("=======")
progresses = [90, 90, 90, 90, 91, 91]
speeds = [5, 4, 3, 2, 1, 1]
print(solution(progresses, speeds))
# [2, 3, 4, 5, 9, 10]
# 1 1 1 1 1 1
