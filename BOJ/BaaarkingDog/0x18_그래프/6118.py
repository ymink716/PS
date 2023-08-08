# 숨바꼭질
# https://www.acmicpc.net/problem/6118

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n + 1)  # 최단거리 테이블

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작점 (비용, 노드)
    distance[start] = 0

    while q:
        # 힙에서 가장 최단거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있다면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드들을 확인
        for i in graph[now]:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist + 1 < distance[i]:
                distance[i] = dist + 1  # 최단경로 테이블 갱신하고
                heapq.heappush(q, (dist + 1, i))  # 힙에 넣어줌

dijkstra(1)

max_distance = max(distance[1:])
print(distance.index(max_distance), max_distance, distance.count(max_distance))