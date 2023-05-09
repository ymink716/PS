# 적록색약
# https://www.acmicpc.net/problem/10026

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    visited[x][y] = True
    now = graph[x][y]  # 현재 색깔

    for i in range(4):  # 현재 좌표의 상하좌우를 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:  # 그래프 범위 안에 있고
            if not visited[nx][ny] and graph[nx][ny] == now:  # 방문하지 않음 and 색깔 같음
                dfs(nx, ny)

n = int(input())
graph = []
for _ in range(n):
    line = list(map(str, input().strip()))
    graph.append(list(line))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[False] * n for _ in range(n)]
rgb_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            rgb_count += 1

for i in range(n):
    for j in range(n):  # 모든 R을 G로 바꿔줌
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]  # 방문 리스트 초기화
gb_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            gb_count += 1

print(rgb_count, gb_count)
