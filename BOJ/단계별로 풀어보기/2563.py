n = int(input())
board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    y, x = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

answer = 0
for i in range(100):
    answer += board[i].count(1)

print(answer)
