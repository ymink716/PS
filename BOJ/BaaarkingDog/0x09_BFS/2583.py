# 영역 구하기
# https://www.acmicpc.net/problem/2583

from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 직사각형 영역 채우기
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    cnt = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt

result = []

for i in range(m):
    for j in range(n):
        # 직사각형으로 채워지지 않은 영역을 만나면 bfs 수행
        if graph[i][j] == 0:
            cnt = bfs(i, j)
            result.append(cnt)

result.sort()

print(len(result))
print(*result)


"""
[0, 0, 0, 0, 1, 1, 0], 
[0, 1, 0, 0, 1, 1, 0], 
[1, 1, 1, 1, 0, 0, 0], 
[1, 1, 1, 1, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0]
"""