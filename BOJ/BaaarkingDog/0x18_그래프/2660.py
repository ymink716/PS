# 회장뽑기
# https://www.acmicpc.net/problem/2660

import sys
input = sys.stdin.readline

n = int(input())
graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:  # 자기 자신으로 가는 비용은 0
            graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    graph[a][b] = 1  # 친구사이 거리 1
    graph[b][a] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

score = int(1e9)  # 회장 후보의 점수
candidates = []  # 후보자 리스트

for i in range(1, n + 1):
    temp = max(graph[i][1:])  # i번 회원이 다른 회원으로 가는 거리의 최대값 = i번 회원의 점수
    if temp == score:  # i번 회원의 점수 = 회장 후보의 점수
        candidates.append(i)  # 후보자 리스트에 추가
    elif temp < score:  # i번 회원의 점수 < 회장 후보의 점수
        score = temp  # 회장 후보의 점수 갱신
        candidates = [i]  # 후보자 리스트 갱신

print(score, len(candidates))
print(*candidates)