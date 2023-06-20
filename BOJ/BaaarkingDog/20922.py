# 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

d = dict()  # 숫자를 카운트할 딕셔너리
temp = list(set(array))
for e in temp:
    d[e] = 0

# 투 포인터
start = 0
answer = 0
for end in range(n):
    d[array[end]] += 1  # 수열의 end 인덱스에 해당하는 숫자 카운트 +1
    if d[array[end]] > k:  # 해당 숫자의 갯수가 k보다 크면
        while start < end:  # 해당 숫자의 갯수가 k보다 작거나 같을 때까지 start 증가
            d[array[start]] -= 1
            start += 1
            if d[array[end]] <= k:
                break
    answer = max(answer, end - start + 1)  # 최장 연속 부분 수열의 길이 갱신

print(answer)
