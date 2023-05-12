# 노드사이의 거리
# https://www.acmicpc.net/problem/1240

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    q.append((start, 0))

    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, distance = q.popleft()

        if now == end:  # 현재 노드가 찾는 노드라면 거리를 리턴
            return distance

        for i, d in tree[now]:  # 현재 노드에 연결된 노드와 거리를 순회
            if not visited[i]:
                visited[i] = True
                q.append((i, distance + d))  # i번 노드와 거리를 갱신한 값을 큐에 추가

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    i, j, d = map(int, input().split())
    tree[i].append((j, d))  # i, j로 가는 거리 d
    tree[j].append((i, d))

for _ in range(m):
    a, b = map(int, input().split())
    result = bfs(a, b)
    print(result)