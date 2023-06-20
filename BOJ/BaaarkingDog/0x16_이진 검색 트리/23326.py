# 홍익 투어리스트
# https://www.acmicpc.net/problem/23326

# from bisect import bisect_left
# import sys
# input = sys.stdin.readline
#
# n, q = map(int, input().split())
# array = list(map(int, input().split()))
#
# tour_list = set()
# for i in range(n):
#     if array[i] == 1:
#         tour_list.add(i + 1)
#
# now = 1
# for _ in range(q):
#     query = input()
#
#     if query[0] == '1':
#         i = int(query[2])
#         if i in tour_list:
#             tour_list.remove(i)
#         else:
#             tour_list.add(i)
#     elif query[0] == '2':
#         x = int(query[2])
#         now = (now + x) % n
#     else:
#         if not tour_list:
#             print(-1)
#         else:
#             temp = list(tour_list)
#             temp.sort()
#             idx = bisect_left(temp, now)
#             print(temp[idx] - now)