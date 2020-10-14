def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def solution(phone_book):

    phone_book.sort(key=lambda x: (len(x)))

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if check(phone_book[i], phone_book[j]):
                return False
    return True


phone_book = ['119', '97674223', '1195524421']
print(solution(phone_book))

phone_book = ['123','456','789']
print(solution(phone_book))

phone_book = ['12','123','1235','567','88']
print(solution(phone_book))