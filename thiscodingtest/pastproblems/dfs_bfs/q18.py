def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_true(p):
    q = []
    for i in p:
        if i == '(':
            q.append(i)
        else:
            if len(q) > 0:
                q.pop()
            else:
                return False
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    print(index)
    u = p[:index + 1]
    v = p[index + 1:]
    print("==", u, v)
    if check_true(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    return answer

p = "(()())()"
print(solution(p))
print("=======================")

p = ")("
print(solution(p))
print("=======================")

p = "()))((()"
print(solution(p))
print("=======================")


