# 나이트의 이동
# https://www.acmicpc.net/problem/7562

from collections import deque
import sys
input = sys.stdin.readline

# 나이트가 이동하는 8방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(l, graph, start, end):
    q = deque()
    q.append(start)

    # 큐가 빌 때까지 반복
    while q:
        x, y, cnt = q.popleft()  # 현재 나이트 위치에서

        # 나이트가 이동하는 8방향을 확인
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 위치가 범위를 벗어나는 경우
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            # 다음 위치를 아직 방문한적 없음 or 이전 이동 횟수 기록보다 지금 가는 경우가 더 작은 경우
            if graph[nx][ny] == -1 or graph[nx][ny] > cnt + 1:
                graph[nx][ny] = cnt + 1  # 방문 횟수 기록 갱신
                q.append((nx, ny, cnt + 1))  # 큐에 다음 좌표를 넣어줌

    print(graph[end[0]][end[1]])


for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    start = (x, y, 0)

    # 나이트가 이동한 최소 횟수를 담을 그래프 초기화
    graph = [[-1] * l for _ in range(l)]
    graph[x][y] = 0

    end = tuple(map(int, input().split()))

    bfs(l, graph, start, end)