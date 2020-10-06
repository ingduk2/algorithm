n, c = list(map(int, input().split()))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1

    #현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
        if count >= c: #C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
            start = mid + 1
            result = mid # 최적의 결과를 저장
        else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
            end = mid -1

print(result)