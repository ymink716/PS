dx = []
dy = []

for _ in range(3):
    x, y = map(int, input().split())
    dx.append(x)
    dy.append(y)

x4, y4 = 0, 0
for i in range(3):
    if dx.count(dx[i]) == 1:
        x4 = dx[i]
    if dy.count(dy[i]) == 1:
        y4 = dy[i]

print(x4, y4)