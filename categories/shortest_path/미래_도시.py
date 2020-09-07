INF = int(1e9)

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 리스트(그래프) 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 거쳐 갈 노드, 최종 목적지 노드

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)


"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""