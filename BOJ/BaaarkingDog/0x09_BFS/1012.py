# 유기농 배추

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()  # 큐에서 밭의 위치를 꺼내
        for i in range(4):  # 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:  # 1(배추밭) 발견하면
                graph[nx][ny] = 0  # 0으로 만들고
                q.append((nx, ny))  # 큐에 다음 위치 추가
    return


for _ in range(int(input())):  # 각 테스트 케이스만큼 반복
    m, n, k = map(int, input().split())  # 가로, 세로, 배추밭 개수
    graph = [[0] * m for _ in range(n)]  # 그래프 초기화

    for _ in range(k):  # 배추밭 위치 지정
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    # 그래프 순회
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:  # 1(배추밭)을 만나면
                bfs(graph, i, j)  # bfs 수행
                count += 1  # 지렁이 +1

    print(count)