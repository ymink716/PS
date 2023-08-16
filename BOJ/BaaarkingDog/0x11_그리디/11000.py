# 강의실 배정
# https://www.acmicpc.net/problem/11000

import heapq
import sys
input = sys.stdin.readline

n = int(input())

lectures = []
for _ in range(n):
    s, t = map(int, input().split())
    lectures.append((s, t))

lectures.sort()

rooms = []
heapq.heappush(rooms, lectures[0][1])

for i in range(1, n):
    # 다음 강의 시작 시간이 현재 강의실 종료 시간보다 빠르면
    if lectures[i][0] < rooms[0]:
        # 새로운 강의실 추가
        heapq.heappush(rooms, lectures[i][1])
    # 그게 아니면 현재 강의실에서 다음 강의 진행
    else:
        # 현재 강의실 종료 시간 변경을 위해 pop한 후 다음 강의 종료시간 push
        heapq.heappop(rooms)
        heapq.heappush(rooms, lectures[i][1])

print(len(rooms))