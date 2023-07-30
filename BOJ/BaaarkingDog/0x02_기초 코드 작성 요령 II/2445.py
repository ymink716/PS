# 별 찍기 - 8
# https://www.acmicpc.net/problem/2445

n = int(input())

for i in range(1, n + 1):
    print("*" * i + " " * (2 * n - 2 * i) + "*" * i)

for i in range(2, n + 1):
    print("*" * (n - i + 1) + " " * 2 * (i - 1) + "*" * (n - i + 1))