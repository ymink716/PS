import heapq

def dijkstra(distance, graph):
    heap = []
    heapq.heappush(heap, [0, 1])  # 시작 노드 heap에 push [거리, 노드]
    while heap:
        cost, node = heapq.heappop(heap)  # 최단거리 노드
        for c, n in graph[node]:
            if cost + c < distance[n]:
                distance[n] = cost + c  # 최단거리 갱신
                heapq.heappush(heap, [cost + c, n])

def solution(N, road, K):
    distance = [float('inf')] * (N + 1)  # 최단 거리 테이블
    distance[1] = 0  # 시작 노드의 거리 0

    # 각 마을의 연결 정보를 담은 리스트
    graph = [[] for i in range(N + 1)]
    for r in road:
        a, b, c = r  # a 마을에서 b 마을로 가는 비용이 c
        # 양방향
        graph[a].append((c, b))
        graph[b].append((c, a))

    dijkstra(distance, graph)

    return len([x for x in distance if x <= K])





# test case
print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))