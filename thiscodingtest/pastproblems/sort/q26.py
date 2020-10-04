import heapq

n = int(input())
card = []
for i in range(n):
    data = int(input())
    heapq.heappush(card, data)

result = 0

while len(card) != 1:
    print(card)
    one = heapq.heappop(card)
    two = heapq.heappop(card)

    sum_val = one + two
    heapq.heappush(card, sum_val)
    result += sum_val
    print(card)

print(result)
