def solution(stages, n):
    result = []
    stages.sort()
    user = len(stages)

    prevstage = stages[0]
    fail = 0
    count = 1
    # for i in range(1, len(stages)):
    #     print(prevstage, stages[i])
    #     if prevstage != stages[i]:
    #         fail += count / user
    #         print("!= ", fail, count, user)
    #         result.append((prevstage, fail))
    #         fail = 0
    #         user -= count
    #         count = 1
    #     else:
    #         count += 1
    #
    #     prevstage = stages[i]

    for stage in range(1, n+1):
        count = 0
        for i in stages:
            if i == stage:
                count += 1

        print(stage, count , user , count / user)
        result.append([count / user, stage])
        user -= count

    # list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    result.sort(key=lambda x: (-x[0], x[1]))
    answer = []
    # for x, y in result:
    #     answer.append(y)

    answer = [i[1] for i in result]
    return answer


stages = [2, 1, 2, 6, 2, 4, 3, 3]
n = 5
print(solution(stages, n))

stages = [4,4,4,4,4]
n = 4
print(solution(stages, n))