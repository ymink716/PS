import math
import sys

input = sys.stdin.readline

N = int(input())
prev = int(input())
dist = []

for _ in range(N - 1):
    next = int(input())
    dist.append(next - prev)
    prev = next

g = math.gcd(*dist)

answer = 0
for d in dist:
    answer += d // g - 1
print(answer)