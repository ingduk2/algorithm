def check_outline_brown(x, y, brown):
    num_outline = (2 * x) + (2 * y) -4
    if num_outline == brown:
        return True
    return False


def solution(brown, yellow):
    answer = []
    color_sum = brown + yellow
    for x in range(1, color_sum):
        for y in range(1, x + 1):
            if x * y == color_sum and check_outline_brown(x, y, brown):
                return [x, y]


brown = 10
yellow = 2
print(solution(brown, yellow))

brown = 8
yellow = 1
print(solution(brown, yellow))
#
brown = 24
yellow = 24
print(solution(brown, yellow))