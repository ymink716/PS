# 최대 힙
# https://www.acmicpc.net/problem/11279

import heapq
import sys
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -num)
