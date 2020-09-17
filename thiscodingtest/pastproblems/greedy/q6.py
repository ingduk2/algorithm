def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    answer = 0
    time = 0
    index = 0
    while True:
        # print(food_times, time, index)
        if time == k:
            break
        if food_times[index] != 0:
            food_times[index] -= 1
        else:
            index += 1
            if index >= len(food_times):
                index = 0
            continue

        print(food_times, time, index)
        #index
        index += 1
        if index >= len(food_times):
            index = 0

        #time
        time += 1

    for i in range(index, len(food_times)):
        if food_times[i] != 0:
            answer = i
            break

    return answer + 1

food_times = [1, 5, 5, 5, 5, 6, 7]
k = 31
print(solution(food_times, k))

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

food_times = [4, 4, 4]
k = 5
print(solution(food_times, k))

food_times = [10, 1, 1, 1]
k = 5
print(solution(food_times, k))