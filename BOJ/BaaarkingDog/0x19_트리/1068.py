# 트리
# https://www.acmicpc.net/problem/1068

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))  # 각 노드의 부모 노드 리스트
deleted = int(input())  # 지우려는 노드

def dfs(num, array):
    array[num] = -2  # 현재 노드를 삭제 (-1~50과 겹치지 않는 수)
    for i in range(n):
        if num == array[i]:  # 삭제한 노드를 부모로 가지는 노드를 찾아 재귀 호출하여 삭제
            dfs(i, array)

# dfs로 지우려는 노드와 자식 노드들을 제거
dfs(deleted, array)

answer = 0
for i in range(n):
    # 삭제된 노드가 아님 and 해당 노드를 부모로 하는 노드가 없음 (리프노드)
    if array[i] != -2 and i not in array:
        answer += 1
print(answer)

