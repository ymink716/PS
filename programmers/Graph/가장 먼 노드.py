from collections import deque


def solution(n, vertex):
    graph = [[] for _ in range(n)]
    distances = [0] * n
    visited = [False] * n

    for a, b in vertex:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # 시작 노드 방문 처리
    queue = deque([0])
    visited[0] = True

    while queue:
        now = queue.popleft()
        # 현재 노드에서 갈 수 있는 노드들을 순회하면서
        for next in graph[now]:
            # 방문하지 않은 노드라면 방문처리, 큐에 추가
            # 인접 노드의 거리 : 1부터 현재 노드까지의 거리 + 1
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                distances[next] = distances[now] + 1

    return distances.count(max(distances))  # 거리가 최대인 것들 카운트


# test
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))