# 최소 비용 구하기

import heapq
import sys
input = sys.stdin.readline

n = int(input())  # 노드 개수
m = int(input())  # 간선 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a -> b 비용 c

start, end = map(int, input().split())
distance = [int(1e9)] * (n + 1)  # 최단거리 테이블

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작점의 최단 경로는 0, 힙큐에 넣어줌
    distance[start] = 0

    while q:  # 큐가 빌 때까지
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드 꺼내기
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적 있다면
            continue
        for i in graph[now]:  # now와 연결된 노드들 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost  # 최단경로 테이블 갱신
                heapq.heappush(q, (cost, i[0]))  # 힙큐에 넣어줌

dijkstra(start)
print(distance[end])
