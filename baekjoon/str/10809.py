import sys


s = sys.stdin.readline().split()[0]
chk = [-1 for i in range(26)]
for i in range(len(s)):
    if chk[ord(s[i]) - ord('a')] == -1:
        chk[ord(s[i]) - ord('a')] = i

for i in chk:
    print(i, end=' ')
