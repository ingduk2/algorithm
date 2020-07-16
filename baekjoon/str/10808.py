import sys


s = sys.stdin.readline().split()[0]
chk = [0 for i in range(26)]
for i in range(len(s)):
    chk[ord(s[i]) - ord('a')] += 1

for i in chk:
    print(i, end=' ')
