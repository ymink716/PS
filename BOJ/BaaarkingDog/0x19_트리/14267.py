# 회사 문화 1
# https://www.acmicpc.net/problem/14267

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))  # 직속 상사 리스트

# 상사 -> 부하직원 관계로 표현
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    graph[array[i]].append(i + 1)

compliment = [0] * (n + 1)  # 직원들이 박은 칭찬 수치

def dfs(e):
    # 직원 e의 부하직원들 확인
    for i in graph[e]:
        # 직원 e가 받은 칭찬 수치를 부하직원에게 더해줌
        compliment[i] += compliment[e]
        dfs(i)

for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

dfs(1)
print(*compliment[1:])