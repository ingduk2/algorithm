def solution(participant, completion):
    answer = ''
    d = {}
    for p in participant:
        if p in d.keys():
            d[p] = d.get(p) + 1
        else:
            d[p] = 1

    e = {}
    for c in completion:
        if c in e.keys():
            e[c] = e.get(c) + 1
        else:
            e[c] = 1

    for p in d.items():
        if p not in e.items():
            answer = p[0]

    return answer

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']
print(solution(participant, completion))

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
print(solution(participant, completion))

