n = int(input())
arr = list(map(int, input().split()))

arr.sort()
# group = 0
# for i in arr:
#     print(n , i)
#     if n - i > 0:
#         n -= i
#         group += 1
#     else:
#         break;
#
# print(group)

result = 0
count = 0

for i in arr:

    count += 1
    print(count, i)
    if count >= i:
        print("add")
        result += 1
        count = 0
print(result)


