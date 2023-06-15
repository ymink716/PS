# 과자 나눠주기
# https://www.acmicpc.net/problem/16401

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, int(1e9)  # 과자 길이의 범위 최소, 최대
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0  # 리스트에서 현재 과자 길이(mid)로 만들 수 있는 과자의 개수
    for s in snacks:
        if s >= mid:
            cnt += (s // mid)  # 하나의 과자가 여러 개의 mid길이 과자를 만들 수 있으므로 몫을 더해줌

    if cnt >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)