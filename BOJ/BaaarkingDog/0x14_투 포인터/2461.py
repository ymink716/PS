# 대표 선수
# https://www.acmicpc.net/problem/2461

import heapq
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

students = []  # 각 학급 학생들의 능력치를 담을 리스트
for _ in range(n):
    c = sorted(list(map(int, input().split())))  # 학급을 오름차순으로 정렬
    students.append(deque(c))  # deque로 넣어줌

min_stats, max_stats = int(1e9), 0  # 선발된 학생들의 최소/최대 능력치
hq = []  # 선발된 학생들이 담긴 리스트 (힙)

# 각 학급의 능력치가 가장 낮은 학생들을 선발
for i in range(n):
    s = students[i].popleft()
    min_stats = min(min_stats, s)
    max_stats = max(max_stats, s)
    heapq.heappush(hq, (s, i))

result = max_stats - min_stats

# 차이를 좁히기 위해 최소값 올리기
# 능력치 낮은 순으로 시작하기 때문에 최대값을 내릴 수는 없음
while hq:
    # 현재 선발된 리스트에서 가장 낮은 학생, 학급 번호 pop
    prev_min_stats, class_number = heapq.heappop(hq)

    # 해당 학급이 이미 다 pop되어서 비어있다면 더 이상 갱신 불가
    if not students[class_number]:
        break

    # 해당 학급에서 다음으로 낮은 학생 선발해서 힙에 넣어줌
    next_min_stats = students[class_number].popleft()
    heapq.heappush(hq, (next_min_stats, class_number))

    # 최대/최소 능력치, 결과값 갱신
    max_stats = max(max_stats, next_min_stats)
    min_stats = hq[0][0]
    result = min(result, max_stats - min_stats)

print(result)