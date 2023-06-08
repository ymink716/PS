# 파일 합치기 3
# https://www.acmicpc.net/problem/13975

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))

    heapq.heapify(files)  # 리스트를 최소힙으로 변환

    cost = 0
    while len(files) > 1:
        # 크기가 가장 작은 파일 2개를 꺼내 합침
        temp = heapq.heappop(files) + heapq.heappop(files)
        cost += temp  # 비용에 추가
        heapq.heappush(files, temp)  # 합친 파일을 힙에 다시 넣어줌

    print(cost)