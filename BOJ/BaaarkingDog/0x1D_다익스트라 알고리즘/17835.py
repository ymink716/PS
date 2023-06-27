# 면접보는 승범이네
# https://www.acmicpc.net/problem/17835

import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 도시 연결 정보를 역방향으로 지정
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))

# 면접장 리스트
targets = list(map(int, input().split()))


def dijkstra():
    q = []
    # 힙큐에 면접장들을 모두 넣어줌
    for t in targets:
        heapq.heappush(q, (0, t))
        distance[t] = 0

    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 도시 꺼내
        # 해당 도시의 최단 거리 정보가 이미 갱신되어 현재 비용보다 적다면 넘어감
        if distance[now] < dist:
            continue
        # 현재 도시와 연결된 도시들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 도시를 거쳐 다른 도시로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 최단 거리 갱신
                heapq.heappush(q, (cost, i[0]))  # 힙큐에 넣어줌


distance = [int(1e11)] * (n + 1)
city, dist = 0, 0

dijkstra()

for i in range(1, n + 1):
    if dist < distance[i]:
        city, dist = i, distance[i]
print(city)
print(dist)
