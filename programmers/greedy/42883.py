def solution(number, k):
    number = list(map(int, number))
    remove_cnt = 0
    idx = 0
    result = []
    while True:

        if idx == len(number):
            if remove_cnt < k:
                result = result[:len(number) - k]
            break

        if remove_cnt == k:
            result += number[idx:]
            break

        while result and result[-1] < number[idx] and remove_cnt < k:
            result.pop()
            remove_cnt += 1

        result.append(number[idx])
        idx += 1

    return ''.join([str(i) for i in result])



number = "19"
k = 1
print(solution(number, k))

number = "1924"
# 1924
# 924
# 94
k = 2
print(solution(number, k))

number = "1231234"
#1231234
#231234
#31234
k = 3
print(solution(number, k))

number = "4177252841"
#477252841
#77252841
#7752841
#775841
k = 4
print(solution(number, k))

number = "23111145"
#477252841
#77252841
#7752841
#775841
k = 6
print(solution(number, k))

number = "121212121212"
k = 8
print(solution(number, k))


number = "999999999999999999"
k = 8
print(solution(number, k))