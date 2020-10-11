n = int(input())

dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)
    print(dp)
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
        # print("2" , next2)
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
        # print("3" , next3)
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5
        # print("5", next5)

print(dp[n-1])
