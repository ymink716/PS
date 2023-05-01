# 개미굴 https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline

# 트리 형태처럼 계층을 가지게끔 add 함수를 재귀로 반복하면서 넣어줌
# {'B': {'A': {}}, 'A': {'B': {'C': {'D': {}}}, 'C': {}}}
def add(d, arr):
    if len(arr) == 0:
        return

    if arr[0] not in d:
        d[arr[0]] = {}

    add(d[arr[0]], arr[1:])

def print_tree(d, depth):
    for r in sorted(d.keys()):  # 딕셔너리의 키 값을 정렬한 채로 순회
        print("--" * depth + r)  # -- * 깊이 + 해당 방의 먹이 출력
        print_tree(d[r], depth + 1)  # 현재 방에서 다음 깊이에 해당 하는 방을 탐색하며 출력

n = int(input())

d = dict()  # 트리의 계층구조를 파악하기 위한 딕셔너리
for _ in range(n):
    arr = list(map(str, input().split()))
    add(d, arr[1:])  # 맨 앞에 숫자는 제거하고 방에 있는 먹이 정보만 넣어줌

print_tree(d, 0)