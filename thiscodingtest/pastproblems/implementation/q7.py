n = input()
divide = len(n) // 2

print(n , divide)

left = 0
right = 0

for i in range(len(n)):
    num = int(n[i])
    if i < divide:
        print("left" , n[i])
        left += num
    else:
        print("right", n[i])
        right += num

if left == right:
    print("LUCKY")
else:
    print("READY")