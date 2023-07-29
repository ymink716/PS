# 멀티버스 Ⅱ
# https://www.acmicpc.net/problem/18869

from collections import defaultdict
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

space = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))

    # 입력받은 행성들 정렬
    sorted_planets = sorted(list(set(planets)))
    # 행성의 크기 : 행성의 순위
    rank = {sorted_planets[i] : i for i in range(len(sorted_planets))}
    # 튜플에 입력받은 순으로 행성들의 순위 저장
    vector = tuple([rank[i] for i in planets])

    space[vector] += 1

answer = 0
for e in space.values():
    # n개의 우주 중 2개를 한 쌍으로 -> 조합 n C 2
    answer += (e * (e - 1)) // 2
print(answer)


"""
입력받은 행성들: [1, 3, 2]
정렬된 행성들: [1, 2, 3]
행성 크기 : 순위 -> {1: 0, 2: 1, 3: 2}
입력받은 행성순으로 순위 저장: (0, 2, 1)

입력받은 행성들: [12, 50, 31]
정렬된 행성들: [12, 31, 50]
행성 크기 : 순위 -> {12: 0, 31: 1, 50: 2}
입력받은 행성순으로 순위 저장: (0, 2, 1)
"""