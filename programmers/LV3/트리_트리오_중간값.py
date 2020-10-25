from collections import deque

def bfs(graph, start, n):
    visited = [False for _ in range(n + 1)]  # 방문여부
    dist = [0 for _ in range(n + 1)]  # 시작점에서 각 노드까지 거리
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i]:
                continue
            visited[i] = True
            q.append(i)
            dist[i] = dist[now] + 1
    return dist

def solution(n, edges):
    # 트리 초기화
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    # 1. 임의의 점 1에서 가장 먼 노드 X를 찾기 (start)
    start = 1
    result = bfs(graph, start, n)
    for i in range(2, n + 1):
        if result[i] > result[start]:
            start = i

    # 2. X에서 각 노드까지의 거리를 구한다
    cnt = 0
    result = bfs(graph, start, n)
    for i in range(1, n + 1):  # 가장 먼 노드 구하기
        if result[i] > result[start]:
            start = i
    for i in range(1, n + 1):  # 가장 먼 노드의 개수 구하기
        if result[start] == result[i]:
            cnt += 1
    # 2-1 가장 먼 노드가 여러개라면 X와 먼 노드 2개를 선택하면 되므로 가장 먼 거리 리턴
    if cnt >= 2:
        return result[start]
    # 2-2 가장 먼 거리의 노드가 Y 하나라면 다시 Y를 기준으로 탐색

    # 3. Y로부터 각 노드까지의 거리를 찾는다
    cnt = 0
    result = bfs(graph, start, n)
    for i in range(1, n + 1):
        if result[i] > result[start]:
            start = i
    for i in range(1, n + 1):
        if result[start] == result[i]:
            cnt += 1
    # 3-1 가장 먼 노드가 여러개라면 Y 노드와 먼 노드 중 2개를 선택하면 되므로 가장 먼 거리 리턴
    if cnt >= 2:
        return result[start]
    # 3-2 가장 먼 노드가 하나라면 둘 사이의 거리 -1 을 리턴
    return result[start] - 1


# test
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]))


# 문제를 풀다 어려워서 검색을 해보니 트리의 지름에 관한 문제였다.
# 다른 사람의 풀이를 참고했고 트리의 지름에 대해 공부해봐야겠다..