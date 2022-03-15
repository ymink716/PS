import sys

input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key= lambda x: (x[1], x[0]))
now = -1
count = 0
for i in range(n):
    if now > data[i][0]:
        continue
    now = data[i][1]
    count += 1

print(count)
