def check(x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != board[i + x][j + y]:
                count += 1
    return count

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

chess = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
        ]

result = 65
for i in range(n - 7):
    for j in range(m - 7):
        temp = check(i, j)
        if result > temp:
            result = temp
        if result > 64 - temp:
            result = 64 - temp

print(result)
