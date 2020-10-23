def make_list(q):

    while True:
        first = q[0]
        change_cnt = 0
        for paper in q:
            if first[0] < paper[0]:
                q.pop(0)
                q.append(first)
                change_cnt += 1
                break
        if change_cnt == 0:
            break


def solution(priorities, location):
    q = []

    loc = ''
    for i in range(len(priorities)):
        q.append([priorities[i], chr(ord('A') + i)])
        if i == location:
            loc = chr(ord('A') + i)
    answer = 1
    while q:
        make_list(q)
        printing = q.pop(0)
        if printing[1] == loc:
            return answer
        answer += 1


priorities = [2, 1, 3, 2]
location = 2
print("ret",solution(priorities, location))
print("================")
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print("ret",solution(priorities, location))
print("================")
priorities = [1,2,3,4,5]
location = 0
print("ret",solution(priorities, location))

