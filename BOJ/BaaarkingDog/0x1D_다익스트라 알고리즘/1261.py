# 알고스팟
# https://www.acmicpc.net/problem/1261

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
distance = [[-1] * n for _ in range(m)]  # 벽을 깬 횟수를 저장

def bfs(a, b):
    q = deque()
    q.append([a, b])
    distance[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 4가지 방향을 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나는 경우
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if distance[nx][ny] == -1:  # 아직 방문하지 않은 방이라면
                if graph[nx][ny] == 0:  # 벽이 없다면
                    distance[nx][ny] = distance[x][y]  # 이전 좌표에서 벽을 깬 횟수 = 다음 좌표 ~
                    q.appendleft([nx, ny])  # 벽이 없는 곳이 우선적으로 큐에서 나오도록 appendleft
                else:  # 벽이 있다면
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx, ny])

bfs(0, 0)
print(distance[m-1][n-1])

