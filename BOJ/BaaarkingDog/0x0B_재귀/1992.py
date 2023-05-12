# 쿼드트리
# https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
result = ""

def quad_tree(x, y, n):
    global result
    color = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != color:
                result += "("
                quad_tree(x, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                result += ")"
                return

    result += color

quad_tree(0, 0, n)
print(result)