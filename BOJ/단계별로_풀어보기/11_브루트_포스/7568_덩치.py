import itertools

n = int(input())

people = []
for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y, i))

comb = list(itertools.combinations(people, 2))
result = [1 for _ in range(n)]
for data in comb:
    if data[0][0] > data[1][0] and data[0][1] > data[1][1]:
        result[data[1][2]] += 1
    elif data[0][0] < data[1][0] and data[0][1] < data[1][1]:
        result[data[0][2]] += 1

for i in result:
    print(i, end=" ")