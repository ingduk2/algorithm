import sys


s = sys.stdin.readline().rstrip('\n')
result_list = []
for i in range(len(s)):
    result_list.append(s[i:len(s)])
result_list.sort()
for i in result_list:
    print(i)