# 별 찍기 - 2
# https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(n):
    print(" " * (n - (i + 1)) + "*" * (i + 1))