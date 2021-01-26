n = int(input())
data = list(map(int, input().split()))
m = max(data)

total = 0
for i in data:
    total += (i / m * 100)

print(total / n)