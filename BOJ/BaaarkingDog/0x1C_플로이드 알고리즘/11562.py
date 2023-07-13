# 백양로 브레이크
# https://www.acmicpc.net/problem/11562

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 거리를 담을 테이블 초기화

# 자기 자신으로 가는 거리는 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선에 대한 정보 입력 받기
for _ in range(m):
    u, v, b = map(int, input().split())
    # 일방 통행의 경우 v -> u 로 가는 길은 설치해야 하므로 비용 1
    if b == 0:
        graph[u][v] = 0
        graph[v][u] = 1
    # 양방향의 경우 비용 0
    else:
        graph[u][v] = 0
        graph[v][u] = 0

# 모든 지점에서 모든 지점으로 가는 최소 거리 구하기 = 설치할 길의 개수
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

k = int(input())
for _ in range(k):
    start, end = map(int, input().split())
    print(graph[start][end])