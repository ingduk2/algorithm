from bisect import bisect_left, bisect_right

list = [ 'front', 'cdcdc','frost', 'kakao']
print(list)
list.sort()
print(list)

print(bisect_right(list, 'frozz'))
print(bisect_left(list, 'froaa'))
