# 컵라면
# https://www.acmicpc.net/problem/1781

import heapq
import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    d, c = map(int, input().split())
    array.append((d, c))

array.sort()  # 데드라인, 컵라면 개수 순으로 오름차순 정렬

hq = []

# 우선순위 큐에 해당 숙제의 컵라면 개수를 하나씩 push
# 현재 작업의 데드라인이 우선순위 큐의 데드라인보다 작다면
# 우선순위 큐에서 제일 작은 컵라면의 개수를 pop
for d, c in array:
    heapq.heappush(hq, c)
    if d < len(hq):
        heapq.heappop(hq)

print(sum(hq))