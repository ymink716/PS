# 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        t[i][j] += max(t[i+1][j], t[i+1][j+1])

print(t[0][0])