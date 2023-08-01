# 구간 자르기
# https://www.acmicpc.net/problem/2283

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# x 좌표(인덱스)에 몇 개의 구간이 올라가 있는지
array = [0] * 1000001

# 각 구간을 입력 받아 포함하는 x 좌표(array[i])에 +1
for _ in range(n):
    left, right = map(int, input().split())
    for i in range(left, right):
        array[i] += 1

a, b, total = 0, 0, 0
possible = False

while a <= b and b < 1000001:
    if total == k:
        possible = True
        break
    # k 만큼의 길이가 안나오면 끝점 b를 1씩 높여서 해당 길이만큼 증가
    elif total < k:
        total += array[b]
        b += 1
    # k 이상의 길이가 나온다면 시작점 a를 1씩 높여 해당 길이만큼 감소
    else:
        total -= array[a]
        a += 1

if possible:
    print(a, b)
else:
    print('0 0')