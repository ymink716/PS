def dfs(graph, start):
    stack = [start]
    marked = {start}
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if w not in marked:
                stack.append(w)
                marked.add(w)
    return len(marked)


def solution(n, wires):
    # 그래프에 노드 간 연결 정보 저장
    graph = {k: set() for k in range(1, n + 1)}
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)

    answer = n
    # 전선 정보를 순회하면서
    for v1, v2 in wires:
        # 하나씩 연결 관계를 끊어냄
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        # 하나 끊은 그래프를 dfs 탐색
        result = abs(2 * dfs(graph, v1) - n)
        # 끊었던 선을 원래대로
        graph[v1].add(v2)
        graph[v2].add(v1)
        answer = min(answer, result)

    return answer


# tset case
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

"""
연결된 노드의 개수가 m개라면 나머지 한 그룹의 노드 개수는 n-m개 
그럼 두 그룹의 개수 차이는 | (n-m) - m | => | n - 2*m |
"""