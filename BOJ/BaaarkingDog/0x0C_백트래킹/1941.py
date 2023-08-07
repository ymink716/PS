# 소문난 칠공주
# https://www.acmicpc.net/problem/1941

from itertools import combinations
from collections import deque

graph = []
for _ in range(5):
    graph.append(input())

# 조합 하나에 S가 4명 이상 포함되어 있는지 확인
def check_group(comb):
    cnt = 0
    for x, y in comb:
        if graph[x][y] == 'S':
            cnt += 1
    if cnt >= 4:
        return True
    else:
        return False

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 해당 조합이 가로 세로로 인접해 있는지 확인, bfs
def check_adjacent(comb):
    q = deque()
    q.append(comb[0])
    visited = [False] * 7
    visited[0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 좌표가 이 그룹 안에 있다면
            if (nx, ny) in comb:
                next = comb.index((nx, ny))
                # 다음 좌표에 아직 방문하지 않은 경우
                if not visited[next]:
                    q.append((nx, ny))
                    visited[next] = True
    # 7명 모두 방문했다면 true
    if False in visited:
        return False
    else:
        return True

answer = 0
# 5x5 각 좌표에서 7명을 뽑는 조합을 구해서 하나씩 확인
for comb in combinations([(i, j) for i in range(5) for j in range(5)], 7):
    if check_group(comb) and check_adjacent(comb):
        answer += 1
print(answer)