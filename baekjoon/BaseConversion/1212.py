import sys

#  8진수 2진수로 1자리를 2진수로 변환. 앞에부터 해도 될듯?
# 314
# 11001100

n = input()
if len(n) == 1 and int(n[0]) == 0:
    print(0, end='')
else:
    newN = ""
    nonZeroIndex = 0
    for i in range(len(n)):
        if n[i] != '0':
            nonZeroIndex = i
            break

    newN = n[nonZeroIndex: len(n)]
    for i in range(len(newN)):
        num = int(newN[i])
        # convert 2

        binaryList = []
        while num > 0:
            namuge = num % 2
            num = int(num / 2)
            binaryList.append(namuge)
        binaryList.reverse()
        #print(binaryList)
        if len(binaryList) == 2 and i != 0:
            binaryList.insert(0, 0)
        if len(binaryList) == 1 and i != 0:
            binaryList[0:0] = [0, 0]
        if len(binaryList) == 0:
            binaryList[0:0] = [0, 0, 0]

        for j in range(len(binaryList)):
            print(binaryList[j], end='')

    print()

