# 수업
# https://www.acmicpc.net/problem/19700

import sys
input = sys.stdin.readline
import bisect

n = int(input())

students = []
for _ in range(n):
    h, k = map(int, input().split())
    students.append([h, k])

students.sort(reverse=True)  # 키를 기준으로 내림차순 정렬
group = []  # 각 그룹의 인원 수를 담을 리스트

# 키가 큰 사람부터 그룹을 배정
for h, k in students:
    # 정렬을 유지하면서 k를 삽입할 때 가능한 가장 왼쪽 인덱스
    index = bisect.bisect_left(group, k)
    # 조건에 해당하는 그룹이 없는 경우, 새로운 그룹 생성
    if index == 0 or group[0] == k:
        group.insert(0, 1)
    # 찾은 경우, k가 들어갈 index의 바로 왼쪽 옆의 그룹에 인원 추가
    # (정렬 유지, 최대한 기존 그룹에 할당해서 그룹의 수 최소화)
    else:
        group[index - 1] += 1

print(len(group))
