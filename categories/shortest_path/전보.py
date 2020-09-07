import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())  # 노드의 개수, 간선의 개수, 시작 노드
graph = [[] for i in range(n+1)]  # 각 노드에 연결된 노드에 대한 정보를 담은 리스트
distance = [INF] * (n + 1)  # 최단 거리 테이블 (무한으로 초기화)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 c

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드 삽입
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 최단 거리의 노드 정보 꺼내기
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)


count = 0  # 도달할 수 있는 노드의 개수
max_distance = 0  # 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1 을 출력
print(count - 1, max_distance)
