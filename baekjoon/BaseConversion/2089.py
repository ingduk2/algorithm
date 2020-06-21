import sys

# -2진수 음수로 나눌때 // 와 int( / ) 는 다르게 표현.
# print(-1 // -2, int(-1 /-2))
n = int(input())
if n == 0:
    print(0)

result = []
while n != 0:
    remainder = n % -2
    n = n // -2
    if remainder < 0:
        remainder += 2
        n += 1
    result.append(remainder)
result.reverse()
for i in range(len(result)):
    print(result[i], end='')
