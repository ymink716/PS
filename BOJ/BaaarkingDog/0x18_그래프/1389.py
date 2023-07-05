# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 거리를 담을 테이블 초기화
graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 거리는 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보 입력받기 거리 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 모든 지점에서 다른 모든 지점으로 가는 거리 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

user = 0  # 정답 유저 번호
min_k = int(1e9)  # 정답 유저의 케빈 베이컨 수
for i in range(1, n + 1):
    k = sum(graph[i][1:])
    if k < min_k:
        user = i
        min_k = k

print(user)

"""
print(graph)
[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
[1000000000, 0, 2, 1, 1, 2], 6
[1000000000, 2, 0, 1, 2, 3], 7
[1000000000, 1, 1, 0, 1, 2], 5
[1000000000, 1, 2, 1, 0, 1], 5
[1000000000, 2, 3, 2, 1, 0]] 8
"""