loc = input()

x = loc[0]
y = loc[1]
x = ord(x) - ord('a') + 1
y = int(loc[1])

# 8가지 가능
movX = [2, 2, -2, -2, 1, -1, 1, -1]
movY = [1, -1, 1, -1, 2, 2, -2, -2]

count = 0

for i in range(8):
    tempX = x + movX[i]
    tempY = y + movY[i]
    if 1 <= tempX <= 8 and 1 <= tempY <= 8:
        count += 1

print(count)
