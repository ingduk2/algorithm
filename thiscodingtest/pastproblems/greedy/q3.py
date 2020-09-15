line = input()

#묶음을 찾아야함.
# 0001100
# 000 , 00
# 11 1번.
# 0011001100
# 묶음의 수가 작은것의 수

zeroGroup = 0
oneGroup = 0

point = int(line[0])
for i in range(1, len(line)):

    num = int(line[i])
    if point != num:
        if point == 0:
            zeroGroup += 1
        else:
            oneGroup += 1
        point = num

if point == 0:
    zeroGroup += 1
else:
    oneGroup += 1


print(zeroGroup, oneGroup)
print(min(zeroGroup, oneGroup))


