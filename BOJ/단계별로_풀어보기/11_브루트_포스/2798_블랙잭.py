import itertools

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
comb = list(itertools.combinations(data, 3))
answer = 0
for cards in comb:
    total = sum(cards)
    if total <= m and total > answer:
        answer = total
print(answer)
