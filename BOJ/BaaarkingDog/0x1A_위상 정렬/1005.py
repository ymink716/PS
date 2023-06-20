# ACM Craft
# https://www.acmicpc.net/problem/1005

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def topology_sort():
#     q = deque()
#
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     times = [0] + list(map(int, input().split()))
#     indegree = [0] * (n + 1)
#     graph = [[] for _ in range(k + 1)]
#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         indegree[y] += 1
#     w = int(input())
#     print(times, graph)