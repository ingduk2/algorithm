import heapq
def check_scoville(scoville, k):
    for s in scoville:
        if s < k:
            return False
    return True


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        # check all upper k
        if check_scoville(scoville, K):
            break

        min_scoville = heapq.heappop(scoville)
        if min_scoville < K:
            if len(scoville) == 0:
                return -1

            next_scoville = heapq.heappop(scoville)
            heapq.heappush(scoville, min_scoville + (next_scoville * 2))
            answer += 1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))

print("==============================")
scoville = [1, 2, 3, 4, 5, 6]
k = 27
print(solution(scoville, k))

print("==============================")
scoville = [1, 2, 3, 4, 5, 6, 7]
k = 28
print(solution(scoville, k))