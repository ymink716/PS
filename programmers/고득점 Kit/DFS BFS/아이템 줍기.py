from collections import deque

def draw(graph, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if graph[i][j] == 0:
                graph[i][j] = 1
            else:
                graph[i][j] = 0
    return graph

def bfs(graph, visited, start, end):
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        print(x, y)
        if x == end[0] and y == end[1]:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= 50 and 1 <= ny <= 50:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0 for _ in range(51)] for _ in range(51)]

    for r in rectangle:
        graph = draw(graph, r[0], r[1], r[2], r[3])
    for r in rectangle:
        graph = draw(graph, r[0] - 1, r[1] - 1, r[2] - 1, r[3] - 1)

    visited = [[0 for _ in range(51)] for _ in range(51)]

    result = bfs(graph, visited, (characterX, characterY), (itemX, itemY))
    return result




# test
print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
#print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
#print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
#print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
#print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))