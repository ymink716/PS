# 효율적인 해킹
# https://www.acmicpc.net/problem/1325

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # B를 해킹하면 A도 해킹할 수 있다

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque()
    q.append(start)

    cnt = 1  # start를 해킹했을 때 해킹할 수 있는 컴퓨터의 개수
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

    return cnt

answer = []
max_cnt = 0
for i in range(1, n + 1):
    result = bfs(i)
    if result > max_cnt:
        answer = [i]
        max_cnt = result
    elif result == max_cnt:
        answer.append(i)

print(*answer)