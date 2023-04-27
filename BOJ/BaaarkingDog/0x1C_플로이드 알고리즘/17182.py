# 우주 탐사선

import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 행성의 개수, 발사되는 행성 위치

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):  # 플로이드 와샬 알고리즘 수행 (모든 정점의 최단 거리 구하기)
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visited = [False for _ in range(N)]
visited[K] = True
answer = int(1e9)

# 백트래킹으로 행성을 탐색, 모든 행성 방문하면서 최소 시간 구하기
def find_min(curr, cost, count):
    global answer
    if N == count:
        answer = min(answer, cost)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find_min(i, cost + graph[curr][i], count + 1)
            visited[i] = False

find_min(K, 0, 1)
print(answer)