# 학교 탐방하기

import sys
input = sys.stdin.readline

def solution(N, edges):
    # 최악의 코스 초기값은 모든 코스가 내리막길(1)로 구성되어 있다고 가정
    # 최적의 코스 초기값은 모든 코스가 오르막길(0)로 구성되어 있다고 가정
    worst, best = 0, N
    max_parent, min_parent = [i for i in range(N + 1)], [i for i in range(N + 1)]

    def find(x, parent):  # 특정 원소가 속한 집합 찾기
        if x != parent[x]:
            parent[x] = find(parent[x], parent)
        return parent[x]

    def union(a, b, parent):  # 두 원소가 속한 집합 합치기
        a = find(a, parent)
        b = find(b, parent)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for a, b, w in edges:
        if w == 1:  # 내리막길
            if find(a, min_parent) != find(b, min_parent):  # 싸이클 발생 x
                best -= 1  # 최적의 코스 가중치 -1
                union(a, b, min_parent)
        else:  # 오르막길
            if find(a, max_parent) != find(b, max_parent):
                worst += 1  # 최악의 코스 가중치 +1
                union(a, b, max_parent)

    return worst ** 2 - best ** 2

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M + 1)]

result = solution(N, edges)
print(result)