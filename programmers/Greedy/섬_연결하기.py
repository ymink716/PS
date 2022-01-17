def solution(n, costs):
    # 비용을 기준으로 오름차순 Sort
    costs.sort(key=lambda x: x[2])
    visited = [0] * n  # 섬의 방문 여부

    answer = 0
    visited[0] = 1  # 첫 번째 섬은 방문했다고 가정

    # 모든 섬을 방문할 때까지
    while sum(visited) != n:
        # 배열을 순회하면서
        for a, b, cost in costs:
            # 두 섬 중에 하나만 방문한 경우만 연결
            if visited[a] + visited[b] == 1:
                visited[a] = 1
                visited[b] = 1
                answer += cost
                break

    return answer


# test
print(solution(4, [[0,1,1], [0,2,2], [1,2,5], [1,3,1], [2,3,8]]))
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))