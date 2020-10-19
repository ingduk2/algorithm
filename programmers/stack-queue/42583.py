def bridge_weight_sum(bridge_list):
    sum = 0
    for w, t in bridge_list:
        sum += w
    # print("sum", sum)
    return sum

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # truck_weights.sort()
    print(truck_weights)
    bridge_list = []
    while len(truck_weights) + len(bridge_list) > 0:
        print("answer", truck_weights, bridge_list, answer)

        # add time
        for i in range(len(bridge_list)):
            bridge_list[i][1] += 1

        # complete bridge
        if bridge_list and bridge_list[0][1] == bridge_length:
            bridge_list.pop(0)

        if truck_weights and bridge_weight_sum(bridge_list) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge_list.append([truck, 0])

        answer += 1
    print(truck_weights, bridge_list)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))

print("================")
bridge_length = 100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))

print("================")
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))

print("================")
bridge_length = 4
weight = 8
truck_weights = [1,2,3,4,5,6,7,8]
print(solution(bridge_length, weight, truck_weights))