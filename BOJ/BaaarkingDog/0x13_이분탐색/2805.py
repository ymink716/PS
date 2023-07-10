# 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def cut_trees(trees, h):
    result = 0
    for tree in trees:
        if tree > h:
            result += (tree - h)
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

h = 0
# 이분탐색할 값 : 목제절단기 높이
start, end = 1, 1000000000

while start <= end:
    mid = (start + end) // 2
    # 목제절단기 높이를 mid로 설정하여 자른 길이 계산
    now = cut_trees(trees, mid)

    # now가 필요한 길이 m 보다 크거나 같다면
    if m <= now:
        h = mid
        start = mid + 1  # 최대값을 구하기 위해 start를 오른쪽으로
    else:  # 그게 아니면 end를 왼쪽으로 옮겨 더 작은 범위 탐색
        end = mid - 1

print(h)