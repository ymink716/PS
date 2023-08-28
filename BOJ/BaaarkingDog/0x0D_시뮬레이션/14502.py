# 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(walls, graph):
    q = deque()

    # 3개의 벽을 세우기
    for (i, j) in walls:
        graph[i][j] = 1

    # 큐에 바이러스(2) 위치를 넣어줌
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 다음 좌표가 빈 공간인 경우 바이러스 전파, 큐에 다음 좌표 넣어줌
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

# 빈 공간의 좌표를 담을 리스트
empty = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 0]
answer = 0

# 각 조합에 대해 벽을 세우고, bfs로 바이러스 전파한 후, 최대값(answer) 갱신
for w in combinations(empty, 3):
    result = bfs(w, copy.deepcopy(data))
    answer = max(answer, result)

print(answer)