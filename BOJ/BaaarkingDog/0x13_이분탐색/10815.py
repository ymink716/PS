# 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = []
m = int(input())
for target in list(map(int, input().split())):
    possible = 0
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            possible = 1
            break
    result.append(possible)

print(*result)

"""
n = int(input())
d = dict()

for a in map(int, input().split()):
    d[a] = 1

m = int(input())
answer = ""
for b in map(int, input().split()):
    if d.get(b):
        answer += "1 "
    else:
        answer += "0 "

print(answer)
"""