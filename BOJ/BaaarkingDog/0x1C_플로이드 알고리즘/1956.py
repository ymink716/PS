# 운동
# https://www.acmicpc.net/problem/1956

import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
# 거리를 담은 테이블, 무한대로 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 모든 지점에서 다른 모든 지점으로 가는 최소 거리 구하기
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 사이클 발생 = 자기 자신 -> 자기 자신으로 돌아옴, 이 중 최소값 구하기
answer = INF
for i in range(1, v + 1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)