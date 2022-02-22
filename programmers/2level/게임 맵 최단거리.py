from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # N x M
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동
    visited = [[0] * m for _ in range(n)]  # 방문 여부
    visited[0][0] = 1  # 시작점
    q = deque()  # bfs를 위한 큐
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        # 최종 경로 도착
        if x == n - 1 and y == m - 1:
            return visited[x][y]

        # 4가지 방향에 대해서 방문 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 좌표가 범위 안에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 좌표가 아직 방문하지 않았고 지나갈 수 있는 자리라면
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1  # 몇 번재 방문인지
                    q.append((nx, ny))
    return -1  # 상대 팀 진영에 도달할 수 없는 경우


# test case
print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1]]))