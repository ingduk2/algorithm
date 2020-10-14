from collections import defaultdict
def solution(clothes):
    answer = 1

    hash_map = defaultdict(lambda: 0)
    for value, key in clothes:
        hash_map[key] += 1

    for v in hash_map.values():
        answer *= v + 1

    return answer - 1