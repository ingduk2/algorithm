import sys


while True:
    s = sys.stdin.readline().rstrip('\n')
    if s == '':
        break
    lower = 0
    upper = 0
    num = 0
    white = 0

    for i in range(len(s)):
        if s[i] == ' ':
            white += 1
        elif ord('a') <= ord(s[i]) <= ord('z'):
            lower += 1
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            upper += 1
        elif ord('0') <= ord(s[i]) <= ord('9'):
            num += 1
    print(lower, upper, num, white)

