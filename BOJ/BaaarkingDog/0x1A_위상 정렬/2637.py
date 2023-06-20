# 장난감 조립
# https://www.acmicpc.net/problem/2637

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0] * (n + 1)  # 진입 차수
graph = [[] for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]  # 각 제품을 만들 때 필요한 부품

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))  # x를 만들기 위한 y의 개수 k -> y에서 x로 가는 가중치 k
    indegree[x] += 1  # 진입 차수 +1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:  # 진입 차수가 0인 노드를 큐에 넣어줌
        q.append(i)

# 큐가 빌 때 까지 반복
while q:
    now = q.popleft()  # 큐에서 원소를 꺼내
    for next, cnt in graph[now]:  # 현재 노드의 연결 정보를 확인
        if needs[now].count(0) == n + 1:  # 현재 노드가 기본 부품이면
            needs[next][now] += cnt  # 가중치(cnt)만큼 더해줌
        else:  # 현재 노드가 중간 부품이면
            for i in range(1, n + 1):  # 현재 노드의 부품들*가중치 만큼 더해줌
                needs[next][i] += needs[now][i] * cnt

        indegree[next] -= 1  # 다음 노드의 진입 차수 -1
        if indegree[next] == 0: # 다음 노드의 진입 차수가 0이면 큐에 넣어줌
            q.append(next)

# n번 노드의 필요 부품들을 확인
for node, cnt in enumerate(needs[n]):
    if cnt > 0:
        print(node, cnt)

# print(*needs)
"""
[[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 2, 2, 0, 0, 0, 0, 0], 
[0, 4, 4, 3, 4, 0, 0, 0], 
[0, 16, 16, 9, 17, 0, 0, 0]]
"""