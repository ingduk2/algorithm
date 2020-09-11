def sequential_search(n, target, array):
    for i in range(n):
        if( array[i] == target):
            return i + 1

print("input : n , target")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("list input")
array = input().split()
print(array, type(array))

print(sequential_search(n, target, array))