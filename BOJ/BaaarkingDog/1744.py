# 수 묶기
# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
positive = []  # 양수를 저장할 리스트
negative = []  # 음수, 0을 저장할 리스트
result = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        positive.append(num)
    elif num == 1:  # 1은 더하는게 값을 크게 만든다 (3 * 1 < 3 + 1)
        result += num
    else:
        negative.append(num)

positive.sort(reverse=True)  # 큰 수 부터 곱해지도록 나오도록 내림차순 정렬
negative.sort()  # 작은 수 부터 곱해지도록 오름차순 정렬

# 양수에 대한 처리
for i in range(0, len(positive), 2):
    if i + 1 >= len(positive):
        result += positive[i]
    else:
        result += positive[i] * positive[i + 1]

# 음수에 대한 처리
# 음수 * 음수 = 양수 절대값 큰 순으로 두 개씩 곱한다
# 마지막에 남은 음수 값과 0이 있다면 둘을 곱해 0을 만들면 값이 작아지지 않음
for i in range(0, len(negative), 2):
    if i + 1 >= len(negative):
        result += negative[i]
    else:
        result += negative[i] * negative[i + 1]

print(result)