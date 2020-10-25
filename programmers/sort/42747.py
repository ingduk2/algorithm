def solution(citations):
    answer = 0
    n = len(citations)
    h = 1
    h_cnt = 0

    while True:
        if h > n:
            break

        for c in citations:
            if c >= h:
                h_cnt += 1

        remain = n - h_cnt
        # print(remain, h_cnt, h)
        if h_cnt >= h >= remain:
            answer = max(answer, h)

        h += 1
        h_cnt = 0

    # print(citations)
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))