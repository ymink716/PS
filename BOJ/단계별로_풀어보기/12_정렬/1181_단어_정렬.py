n = int(input())

data = []
for _ in range(n):
    s = input()
    if data.count(s) == 0:
        data.append(s)

data.sort(key=lambda x: (len(x), x))

for s in data:
    print(s)