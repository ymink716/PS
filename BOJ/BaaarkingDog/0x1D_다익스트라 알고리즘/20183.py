# 골목 대장 호석 - 효율성 2
# https://www.acmicpc.net/problem/20183

import heapq
import sys

input = sys.stdin.readline
INF = int(1e14) + 1

n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dijkstra(limit):
    # 우선순위 큐 초기화
    hq = []
    heapq.heappush(hq, (0, a))
    # 최단거리 테이블 초기화
    distance = [INF] * (n + 1)
    distance[a] = 0

    # 큐가 빌 때까지 반복
    while hq:
        # 가장 최단 거리가 짧은 노드 꺼내기
        now_cost, now = heapq.heappop(hq)

        # 이미 처리된 적 있으면 넘어감
        if distance[now] != now_cost:
            continue

        # 현재 노드와 연결된 노드들을 확인
        for i in graph[now]:
            next, next_cost = i
            # 제한 비용보다 크면 넘어감
            if next_cost > limit:
                continue
            cost = now_cost + next_cost
            # 현재 노드를 거쳐서 가는 비용이 더 작으면
            if cost < distance[next]:
                distance[next] = cost  # next 노드의 최단거리 테이블 갱신
                # 다음 노드가 도착지 and 다음 노드의 최단거리 비용이 가진 금액보다 작거나 같음
                if next == b and distance[next] <= c:
                    return True
                heapq.heappush(hq, (cost, next))

    return distance[b] <= c

costs = []  # 간선 비용을 담을 pq
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))
    heapq.heappush(costs, -d)

# 이분탐색할 값 : 간선을 지나가는 제한 비용
left, right = 0, -heapq.heappop(costs)
answer = INF  # 간선을 지나가는 비용의 최대값들 중 최소값..

while left <= right:
    mid = (left + right) // 2
    # mid 비용 이하로 간선을 통과할 수 있다면
    if dijkstra(mid):
        answer = min(answer, mid)
        right = mid - 1  # 최소값을 찾으므로 오른쪽 범위를 줄인다
    else:
        left = mid + 1

if answer == INF:
    print(-1)
else:
    print(answer)