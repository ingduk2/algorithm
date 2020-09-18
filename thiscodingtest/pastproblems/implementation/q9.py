def solution(s):
    result = 0

    answer = len(s)
    for c in range(1, len(s)//2 + 1):
        newstring = ""
        prev = s[0:c]
        count = 1
        for index in range(c, len(s), c):
            print(prev)

            if prev == s[index:index+c]:
                count += 1
            else:
                newstring+= str(count) + prev if count > 1 else prev
                prev = s[index:index+c]
                count = 1
        newstring+= str(count) + prev if count > 1 else prev
        print("==", newstring)
        answer = min(answer, len(newstring))


    return answer

s = "aabbaccc"
print(solution(s))

s = "abcabcdede"
print(solution(s))
#
s = "ababcdcdababcdcd"
print(solution(s))

s = "xababcdcdababcdcd"
print(solution(s))

