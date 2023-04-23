def dfs(computers, visited, i):
    # 방문 여부 갱신
    if visited[i] == False:
        visited[i] = True
    # i번 컴퓨터의 연결 정보를 순회
    for j in range(len(computers[i])):
        # i와 j 컴퓨터가 연결되어 있고 j가 아직 방문하지 않았다면
        if computers[i][j] == 1 and visited[j] == False:
            dfs(computers, visited, j)  # j에 대하여 탐색 진행

def solution(n, computers):
    visited = [False] * n  # 각 컴퓨터 방문 여부
    answer = 0
    # n개 컴퓨터를 순회하면서
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면
        if visited[i] == False:
            dfs(computers, visited, i)  # i번 컴퓨터에 대한 탐색
            answer += 1  # 네트워크 +1
    return answer


# test
c1 = [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]
print(solution(3, c1))

c2 = [[1, 1, 0],
      [1, 1, 1],
      [0, 0, 1]]
print((solution(3, c2)))

