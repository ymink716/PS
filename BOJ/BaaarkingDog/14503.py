# 로봇 청소기
# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 4방향, 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 방향에서 90도 회전
def rotate(d):
    if d == 0: return 3
    elif d == 1: return 0
    elif d == 2: return 1
    elif d == 3: return 2

cnt = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
    if graph[r][c] == 0:
        graph[r][c] = -1
        cnt += 1

    possible = False
    # 현재 칸의 주변 4칸을 확인
    for _ in range(4):
        d = rotate(d)  # 반시계 방향 90도 회전
        nx = r + dx[d]
        ny = c + dy[d]
        # 다음 좌표가 범위 안에 있음 and 다음 좌표가 아직 청소되지 않음
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            r, c = nx, ny  # 한 칸 전진
            possible = True
            break

    # 청소되지 않은 빈칸이 없는 경우
    if not possible:
        # 후진할 다음 좌표
        nx = r - dx[d]
        ny = c - dy[d]

        # 벽이 아니면 후진
        if graph[nx][ny] != 1:
            r, c = nx, ny
            continue
        # 후진할 수 없으면 종료
        else:
            break

print(cnt)