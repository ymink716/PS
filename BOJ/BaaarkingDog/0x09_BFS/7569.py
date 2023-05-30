# 토마토
# https://www.acmicpc.net/problem/7569

from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())  # 가로, 세로, 높이
# 창고에 쌓인 토마토 3차원 리스트로 입력
warehouse = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 상 하 좌 우 앞 뒤 6방향 설정
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

visited = [[[False] * m for _ in range(n)] for _ in range(h)]
q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 다음 토마토가 안 익음 and 아직 방문하지 않음
            if warehouse[nz][nx][ny] == 0 and visited[nz][nx][ny] == False:
                q.append((nz, nx, ny))  # 큐에 다음 좌표 넣어주고
                warehouse[nz][nx][ny] = warehouse[z][x][y] + 1  # = 이전 좌표 + 1
                visited[nz][nx][ny] = True  # 방문 처리

# 먼저 창고를 확인하면서 모든 익은 토마토(1)을 큐에 넣어줌
for k in range(h):
    for i in range(n):
        for j in range(m):
            if warehouse[k][i][j] == 1 and visited[k][i][j] == False:
                q.append((k, i, j))
                visited[k][i][j] = True

bfs()  # bfs 알고리즘 수행

answer = 0

# 다시 창고를 확인하면서 안익은 토마토가 있다면 -1 출력 후 종료
# 줄 단위로 answer 갱신
for box in warehouse:
    for row in box:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(row))

# 익은 토마토는 1부터 시작하므로 일수는 -1
# 처음부터 모두 1이었다면 1 - 1 = 0
print(answer - 1)