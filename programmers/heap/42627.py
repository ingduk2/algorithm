import heapq

def solution2(jobs):
    answer, nztime = 0, 0
    new = len(jobs)
    jobs.sort()

    while jobs:
        print("jobs", jobs, nztime)
        if nztime >= jobs[0][0]:
            tmp = sorted(list(filter(lambda x: x if x[0] <= nztime else False, jobs)),key=lambda x: x[1])
            print("tmp",tmp)
            tp = heapq.heappop(tmp)
            print("tp", tp)
            nztime += tp[1]
            answer += nztime-tp[0]
            print("time", nztime, answer)
            jobs = tmp + jobs[len(tmp)+1:]
        else : nztime = jobs[0][0]

    return int(answer/new)

def solution(jobs):
    answer = 0

    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[0])

    end = jobs[0][0]
    full_time = end

    while jobs:
        pq = []
        for i in range(len(jobs)):
            if jobs[i][0] <= end:
                pq.append(jobs[i])
        # print("pq", pq, "jobs", jobs)
        pq = sorted(pq, key=lambda x:x[1])
        if len(pq) == 0:
            end = jobs[0][0]
            full_time = end
        else:
            pop = heapq.heappop(pq)
            # print("pop", pop)
            jobs.remove(pop)
            full_time += pop[1]
            answer += full_time - pop[0]
            # print("time", full_time, answer)
            end += pop[1]

    return answer // length

# 0 3 3 3
# 1 9 12 15
# 2 6 18 33

# 0 3 3 3
# 2 6 9 12
# 1 9 18 30

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("=========================")
jobs = [[0, 3], [1,2], [10,5]]
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("==========================")
jobs = [[0,4], [0,3], [0,2], [0,1]]
# 1, 2, 3, 4
# 1, 3, 6, 10 20 / 4 = 5
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("==========================")
jobs = [[3,6], [3,1], [1,2], [0,1]]
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("==========================")
jobs = [[0, 3], [1, 9], [500, 6]]
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("==========================")
jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
print(solution(jobs))
print("answer")
print(solution2(jobs))
print("============================")
jobs = [[0, 10], [2, 3], [9, 3]]
print(solution(jobs))
print("answer")
print(solution2(jobs))