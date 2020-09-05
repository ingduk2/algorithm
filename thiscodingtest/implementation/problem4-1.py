n = int(input())
command = list(map(str, input().split()))

result = [1, 1]


def check(x, y, limit):
    if 1 <= x <= limit and 1 <= y <= limit:
        return True
    else:
        return False


for plan in command:
    print(plan)
    if plan == 'L':
        if check(result[0], result[1] - 1, n):
            result[1] -= 1
    elif plan == 'R':
        if check(result[0], result[1] + 1, n):
            result[1] += 1
    elif plan == 'U':
        if check(result[0] - 1, result[1], n):
            result[0] -= 1
    elif plan == 'D':
        if check(result[0] + 1, result[1], n):
            result[0] += 1

print(result[0], result[1])
