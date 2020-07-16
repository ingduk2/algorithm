import sys


s = sys.stdin.readline().rstrip('\n')
sub = ord('z') - ord('a') + 1
result = ''
for i in range(len(s)):
    if ord('a') <= ord(s[i]) <= ord('z'):
        if ord(s[i]) + 13 > ord('z'):
            result += chr(ord(s[i]) + 13 - sub)
        else:
            result += chr(ord(s[i]) + 13)
    elif ord('A') <= ord(s[i]) <= ord('Z'):
        if ord(s[i]) + 13 > ord('Z'):
            result += chr(ord(s[i]) + 13 - sub)
        else:
            result += chr(ord(s[i]) + 13)
    elif s[i] == ' ':
        result += ' '
    else:
        result += s[i]
print(result)