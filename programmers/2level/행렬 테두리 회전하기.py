def solution(rows, columns, queries):
    graph = [[] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for _ in range(columns):
            graph[i].append(num)
            num += 1

    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        now = graph[x1][y1]
        changed = []
        for i in range(1, y2 - y1 + 1):
            temp = graph[x1][y1 + i]
            graph[x1][y1 + i] = now
            now = temp
            changed.append(now)
        for i in range(1, x2 - x1 + 1):
            temp = graph[x1 + i][y2]
            graph[x1 + i][y2] = now
            now = temp
            changed.append(now)
        for i in range(1, y2 - y1 + 1):
            temp = graph[x2][y2 - i]
            graph[x2][y2 - i] = now
            now = temp
            changed.append(now)
        for i in range(1, x2 - x1 + 1):
            temp = graph[x2 - i][y1]
            graph[x2 - i][y1] = now
            now = temp
            changed.append(temp)
        answer.append(min(changed))

    return answer


# test
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97,	[[1, 1, 100, 97]]))