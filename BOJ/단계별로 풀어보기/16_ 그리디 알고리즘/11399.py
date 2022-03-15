n = int(input())
data = list(map(int, input().split()))

data.sort()
time = 0
answer = 0
for p in data:
    time += p
    answer += time

print(answer)