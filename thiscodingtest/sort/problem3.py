n = int(input())

arr = []
for i in range(n):
    line = input().split()
    arr.append((line[0], line[1]))

arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')