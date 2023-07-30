# 별 찍기 - 9
# https://www.acmicpc.net/problem/2446

n = int(input())

for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * (2 * (n - i) + 1))

for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))