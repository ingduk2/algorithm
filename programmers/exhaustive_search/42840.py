def solution(answers):
    answer = []

    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    index1 = 0
    index2 = 0
    index3 = 0
    for i in range(len(answers)):
        #people1
        if answers[i] == people1[index1%len(people1)]:
            cnt1 += 1

        #people2
        if answers[i] == people2[index2%len(people2)]:
            cnt2 += 1

        #people3
        if answers[i] == people3[index3%len(people3)]:
            cnt3 += 1

        index1 += 1
        index2 += 1
        index3 += 1

    result = [[1, cnt1], [2, cnt2], [3, cnt3]]
    max_cnt = max(cnt1, cnt2, cnt3)
    for p, c in result:
        if max_cnt == c:
            answer.append(p)

    return answer

answers = [1,2,3,4,5]
print(solution(answers))

answers = [1,3,2,4,2]
print(solution(answers))

