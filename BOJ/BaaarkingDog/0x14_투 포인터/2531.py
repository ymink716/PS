# 회전 초밥
# https://www.acmicpc.net/problem/2531

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array = array + array  # 회전되므로 회전초밥 리스트를 이어 붙임
dishes = array[:k] + [c]  # 먹은 접시 리스트 초기화
answer = len(set(dishes))
dishes.pop()

for i in range(1, n):  # 회전 초밥 리스트를 순회
    dishes.pop(0)  # 먹은 접시 리스트에서 맨 앞 그릇이 빠지고
    dishes.append(array[i + k - 1])  # 회전 초밥 리스트의 다음 접시 추가
    dishes.append(c)  # 쿠폰 접시 추가
    answer = max(answer, len(set(dishes)))  # 최대값 구하기
    dishes.pop()  # 쿠폰 접시 빼기

print(answer)