# 문자열 지옥에 빠진 호석
# https://www.acmicpc.net/problem/20166

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

likes, result = [], {}
for _ in range(k):
    s = input().rstrip()
    likes.append(s)
    result[s] = 0

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

def dfs(x, y, cnt, s):
    if cnt > 5:
        return
    # 지금까지 탐색한 문자열이 좋아하는 문자열들 중에 있다면
    if s in result:
        result[s] += 1

    # 8가지 방향에 대해서 재귀 호출
    for i in range(8):
        nx = (x + dx[i] + n) % n
        ny = (y + dy[i] + m) % m
        dfs(nx, ny, cnt + 1, s + graph[nx][ny])

# 그래프 전체를 순회하면서 각 좌표를 시작점으로 dfs 알고리즘 수행
for i in range(n):
    for j in range(m):
        dfs(i, j, 1, graph[i][j])

# 좋아하는 문자열 리스트에서 순서대로 딕셔너리를 확인. 개수를 출력
for like in likes:
    print(result[like])