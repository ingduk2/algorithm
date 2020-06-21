import sys


# 17 8
# 2
# 2 16
# 6 2

def makeorinum(ori, orilist):
    orinum = 0
    counter = len(orilist) - 1
    for i in range(len(orilist)):
        orinum += orilist[i] * (ori ** counter)
        counter -= 1
    return orinum


def makenewnum(new, orinum):
    newnum = []
    while orinum != 0:
        remainder = orinum % new
        orinum = orinum // new
        newnum.append(remainder)
    newnum.reverse()
    return newnum


a, b = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))
orinum = makeorinum(a, numbers)
resultlist = makenewnum(b, orinum)
for i in range(len(resultlist)):
    print(resultlist[i], end=' ')
