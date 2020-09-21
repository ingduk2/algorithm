def check_kidung_upper(dx, dy, answer):
    for i in answer:
        x, y, a = i
        if dx == x and dy == y and a == 0:
            return True
    return False

def check_kidung_between_bo(dx, dy, answer):
    for i in answer:
        x, y, a = i
        if dx == x and dy == y and a == 1:
            return True
    return False


def check_end_bo(dx, dy, answer):
    dx -= 1
    for x, y, a in answer:
        if [x-1, y, 1] in answer:
            print("aaa1")
        if (dx == x and dy == y and a == 1):
            print("aaa11")

        if (dx == x and dy == y and a == 1) or (dx + 1 == x and dy == y and a == 1):
            return True
    return False



def fullcheck(answer):
    result = True
    for i in answer:
        x, y, a = i
        if a == 0:
            if y == 0 or check_end_bo(x, y, answer) or check_kidung_upper(x, y - 1, answer):
                result &= True
            else:
                result &= False
        if a == 1:
            if check_kidung_upper(x, y - 1, answer) or check_kidung_upper(x + 1, y - 1, answer) or (
                    check_kidung_between_bo(x - 1, y, answer) and check_kidung_between_bo(x + 1, y, answer)):
                result &= True
            else:
                result &= False
    return result



def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        # a: 0 기둥, 1 보
        # b: 0 삭제 1 설치

        #설치 기둥인 경우 (바닥 위 , 보의 한쪽 끝, 기둥 위)
        if a == 0 and b == 1:
            if y == 0 or check_end_bo(x, y, answer) or check_kidung_upper(x, y-1, answer):
                answer.append([x, y, a])

        #설치 보인 경우 (한쪽 끝이 기둥 위, 양쪽 끝이 보와동시에 연결.)
        if a == 1 and b == 1:
            # 두 개가 기둥인지 체크.
            if check_kidung_upper(x, y - 1, answer) or check_kidung_upper(x + 1, y - 1, answer) or (check_kidung_between_bo(x - 1, y, answer) and check_kidung_between_bo(x + 1, y, answer)):
                answer.append([x, y, a])

        #삭제 기둥
        if a == 0 and b == 0:
            answer.remove([x, y, a])
            if not fullcheck(answer):
                answer.append([x, y, a])

        #삭제 보
        if a == 1 and b == 0:
            answer.remove([x, y, a])
            if not fullcheck(answer):
                answer.append([x, y, a])


    answer.sort()
    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))