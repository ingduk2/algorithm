arr = []
arr.append(1)
arr.append("1")
print(arr)

line = input()

alpas = []
numbers = []

for i in line:
    if i.isalpha():
        alpas.append(i)
    else:
        numbers.append(int(i))

alpas.sort()
alpas.append(sum(numbers))
for i in alpas:
    print(i, end='')