import sys

#  2진수 8진수 2진수 3개씩 끊어서 2진수로 계산 후 append

n = input()
counter = 0
eachNum = 0
resultList = []
for i in range(len(n)-1, -1, -1):
    if counter > 2:
        counter = 0
        resultList.append(eachNum)
        eachNum = 0
    eachNum += int(n[i]) * (2 ** counter)
    counter += 1
resultList.append(eachNum)

for i in range(len(resultList)-1, -1, -1):
    print(resultList[i], end='')
print()
