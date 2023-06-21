# 우주신과의 교감
# https://www.acmicpc.net/problem/1774

import math
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())  # 노드의 개수, 이미 연결된 간선의 개수
parent = [i for i in range(n + 1)]  # 부모 테이블 초기화

location = [(-1, -1)]  # 노드들의 좌표
for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

for _ in range(m):  # 이미 연결된 노드들 union
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges = []
# 모든 간선에 대한 정보 구하기
for a in range(1, n):
    for b in range(a, n + 1):
        p, q = location[a], location[b]  # a, b 노드의 좌표
        distance = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)  # 두 점 사이의 거리
        edges.append((distance, a, b))

edges.sort()  # 거리 순으로 오름차순 정렬

answer = 0
for edge in edges:  # 간선들을 확인하면서
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost  # 새로 연결되는 간선의 거리를 더해줌

print("{:.2f}".format(answer))