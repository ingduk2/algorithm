def solution(numbers):
    numbers = sorted(numbers, key=lambda x:str(x), reverse=True)
    # print(numbers)
    for i in range(len(numbers)):
        num1 = str(numbers[i])
        if len(num1) >= 2 and i != len(numbers) - 1:
            num2 = str(numbers[i + 1])
            if int(num1+num2) < int(num2+num1):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    # print(numbers)
    if sum(numbers) == 0:
        return 0
    else:
        return ''.join([str(i) for i in numbers])



numbers = [10,101]
print(solution(numbers))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

numbers = [3, 32, 34, 5, 9, 2, 1]
print(solution(numbers))