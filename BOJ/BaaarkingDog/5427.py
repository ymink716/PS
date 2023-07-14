# 불
# https://www.acmicpc.net/problem/5427

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        now = visited[x][y]

        for i in range(4):  # 4가지 방향을 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음방향이 범위 안에 있을 때
            if 0 <= nx < h and 0 <= ny < w:
                # 아직 방문한적이 없고 이동가능이거나 시작위치인 경우
                if visited[nx][ny] == -1 and (graph[nx][ny] == '.' or graph[nx][ny] == '@'):
                    # now가 불인 경우 다음 방향도 불
                    if now == 'F':
                        visited[nx][ny] = now
                    # now가 이동경로인 경우 다음 방향 now +1
                    else:
                        visited[nx][ny] = now + 1
                    # 큐에 다음 방향을 넣어줌
                    q.append((nx, ny))
            # 범위를 벗어난 경우
            else:
                # 현재 값이 불이 아니라면 탈출 성공
                if now != 'F':
                    return now + 1

    return 'IMPOSSIBLE'

for _ in range(int(input())):
    w, h = map(int, input().split())

    graph = []
    for _ in range(h):
        graph.append(list(input().strip()))

    visited = [[-1] * w for _ in range(h)]
    q = deque()
    start = None

    for i in range(h):
        for j in range(w):
            # 불의 위치에 대한 방문 리스트 처리 후 먼저 큐에 넣어줌
            if graph[i][j] == '*':
                visited[i][j] = 'F'
                q.append((i, j))
            # 시작 위치에 대한 방문 리스트 처리
            elif graph[i][j] == '@':
                visited[i][j] = 0
                start = (i, j)

    # 시작 위치는 불의 위치를 다 넣고 난 후에 큐에 넣어줌
    # bfs이기 때문에 불이 1칸씩 먼저 번지고, 상근이가 한 칸 이동하는 사이클이 반복
    q.append(start)
    print(bfs())