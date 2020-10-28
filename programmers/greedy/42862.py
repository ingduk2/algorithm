def solution(n, lost, reserve):
    answer = 0
    reserve_list = [[0,0]]

    for i in range(1, n + 1):
        res = 1
        if i in reserve:
            res += 1
        if i in lost:
            res -= 1
        reserve_list.append([i, res])

    print(reserve_list)

    for num, r in reserve_list[1:]:
        print(num, r, "===", num -1, num + 1)
        if r == 0:
            if num - 1 > 0 and reserve_list[num - 1][1] == 2:
                reserve_list[num - 1][1] -= 1
                reserve_list[num][1] = 1
            if num + 1 <= n and reserve_list[num + 1][1] == 2:
                reserve_list[num + 1][1] -= 1
                reserve_list[num][1] = 1

    print(reserve_list)

    for num, r in reserve_list[1:]:
        if r > 0:
            answer += 1
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))
print("===========================")
n = 5
lost = [2,4]
reserve = [3]
print(solution(n, lost, reserve))
print("===========================")
n = 3
lost = [1]
reserve = [1]
print(solution(n, lost, reserve))
print("===========================")
n = 2
lost = [1]
reserve = [2]
print(solution(n, lost, reserve))
print("===========================")