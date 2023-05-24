# 차집합
# https://www.acmicpc.net/problem/1822

import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a - b
result = list(c)
result.sort()

print(len(result))
print(*result)
