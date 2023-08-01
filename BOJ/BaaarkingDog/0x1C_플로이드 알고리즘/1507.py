# 궁금한 민호
# https://www.acmicpc.net/problem/1507

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

discard = [[False] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue
            # 최소한의 도로로 연결되어 있으므로
            # i - k - j 최단 시간 = i - j 최단 시간 -> i - j 를 삭제
            if graph[i][j] == graph[i][k] + graph[k][j]:
                discard[i][j] = True
            # 불가능한 경우
            # i - j의 최단 시간 > k를 거쳐 가는 시간
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit()

answer = 0
for i in range(n):
    # 양방향 도로로 저장되어 있으므로 한 번만 더하게 인덱스 설정
    for j in range(i + 1, n):
        if not discard[i][j]:
            answer += graph[i][j]
print(answer)