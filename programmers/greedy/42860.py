import copy


def get_move_alpha_cnt(start, end):
    diff = ord(end) - ord(start)
    if diff > 13:
        diff = 26 - diff
    return diff


def check_move(check):
    for c in check:
        if c == False:
            return False
    return True


def min_cursor(name):
    cnt_left_a = 0
    for i in range(1, len(name)):
        if name[i] == 'A':
            cnt_left_a += 1
        else:
            break

    cnt_right_a = 0
    for i in range(len(name) - 1, -1, -1):
        if name[i] == 'A':
            cnt_right_a += 1
        else:
            break
    right_cursor_straight = len(name) - 1 - cnt_right_a
    left_cursor_straight = len(name) - 1 - cnt_left_a


    #A A A J A A A A A A N
    check = []
    for n in name:
        if n == 'A':
            check.append(True)
        else:
            check.append(False)

    # right_turn
    right_turn = 1e8
    for turn in range(1, len(name) - 1, 1):
        check_copy = copy.deepcopy(check)
        # print("turn", turn)
        right_cnt = -1
        idx = 0
        idx_add = 1
        while not check_move(check_copy):
            # print("right turn", name[idx], "turn", turn, "idx", idx, check_copy, check)
            if name[idx] != 'A':
                check_copy[idx] = True

            right_cnt += 1
            if turn == idx:
                idx_add = -1
            idx += idx_add
        right_turn = min(right_turn, right_cnt)

    # left turn
    left_turn = 1e8
    for turn in range(-1, -(len(name)), -1):
        check_copy = copy.deepcopy(check)
        # print("left turn", turn)
        left_cnt = -1
        idx = 0
        idx_add = -1
        while not check_move(check_copy):
            # print("left turn", name[idx], "turn", turn, "idx", idx, check_copy, check)
            if name[idx] != 'A':
                check_copy[idx] = True

            left_cnt += 1
            if turn == idx:
                idx_add = 1
            idx += idx_add
        left_turn = min(left_turn, left_cnt)
    # print("===============cursor", right_cursor_straight, left_cursor_straight, right_turn, left_turn)
    return min(right_cursor_straight, left_cursor_straight, right_turn, left_turn)


def solution(name):
    name_start = 'A' * len(name)
    answer = 0

    for start, end in zip(name_start, name):
        answer +=get_move_alpha_cnt(start, end)

    answer += min_cursor(name)

    return answer


#1 상하 이동, 알파벳이 아래로가는게 가까운지, 위로 가는게 가까운지 확인 후 이동시켜서 만듬.
    # a b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    # 0 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    # 0 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1

    #2 좌우 이동, A가 있다면 어떻게 가는게 최소일지. 들어갔다 나오면 어차피 최소가 아님. 왼쪽시작이냐 오른쪽시작이냐일듯.
    # AAAAAA 0
    # BAAAB  left 1
    # BBBACB 그냥 right 5
    # BACAB left 3 끝.
    # BACCCCCCCCCB
    # BAAACBCBSABB
    # idx 1 부터 연속 A의 개수 구해서 왼쪽개수에서 뺌
    # 잘못생각함. 가다가 반대로 꺾는 경우가 생김.
    # A A A J A A A A A A N

name = "JEROEN"
print(solution(name))

name = "JAAAN"
print(solution(name))

name = "AABAAAAAB"
print(solution(name))

name = "BAABA"
print(solution(name))
#4

name = "ABABA"
print(solution(name))
#5

name = "BABAB"
print(solution(name))
#6

name = "BBABAAAB"
print(solution(name))
#9

name = "AAZAAAZ"
print(solution(name))
#6

