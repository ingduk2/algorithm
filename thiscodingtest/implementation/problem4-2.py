n = int(input())

# 시 , 분 , 초 n 은 시간
count = 0

# h , m , s
for h in range(0, n + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            # print(h, m, s)
            if str(s).find('3') >= 0 or str(m).find('3') >= 0 or str(h).find('3') >= 0:
                # print('====')
                count += 1
print(count)
