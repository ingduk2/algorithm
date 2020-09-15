# S = 0~9
# x , +
# 0 사이는 더하고 , 나머지는 곱하기 집어넣으면 될듯함.

# 20984
# 2 + 0 * 9 * 8 * 4
# 29084
# 2 * 9 + 0 * 8 * 4
# 20004
# 2 + 0 + 0 + 0 * 4
line = input()
oper = []
result = -1
for i in range(len(line)-1):
    print(line[i], line[i+1])
    operation = ''
    num1 = int(line[i])
    num2 = int(line[i+1])

    if ((i == 0 and num1 == 0) or num2 == 0) or ((i == 0 and num1 == 1) or num2 == 1):
        oper.append('+')
        operation = '+'
    else:
        oper.append('*')
        operation = '*'

    if operation == '+':
        if result == -1:
            result = num1 + num2
        else:
            result += num2
    else:
        if result == -1:
            result = num1 * num2
        else:
            result *= num2

print(result)
