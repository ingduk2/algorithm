from itertools import permutations
import math


def is_prime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_list = list(map(int, numbers))
    num_set = set()
    for i in range(1, len(num_list) + 1, 1):
        comb_list = list(permutations(num_list, i))
        for c in comb_list:
            num = int(''.join([str(i) for i in c]))
            num_set.add(num)

    print(num_set)
    for num in num_set:
        if is_prime(num):
            print("Prime", num)
            answer += 1

    return answer

a = set(range(0,10))
print(a)

numbers = "17"
print(solution(numbers))

numbers = "011"
print(solution(numbers))

numbers = "2"
print(solution(numbers))

numbers = "3"
print(solution(numbers))

numbers = "0000000"
print(solution(numbers))
