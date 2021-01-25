data = input()

temp = -1
counts = [0, 0]
for i in data:
    n = int(i)
    if temp != n:
        temp = n
        counts[n] += 1

print(min(counts))
