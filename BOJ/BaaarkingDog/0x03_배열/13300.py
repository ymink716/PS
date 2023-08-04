# 방 배정
# https://www.acmicpc.net/problem/13300

from collections import defaultdict

n, k = map(int, input().split())
d = defaultdict(int)

for _ in range(n):
    s, y = map(int, input().split())
    d[(s, y)] += 1

answer = 0
for i in d.values():
    if i % k == 0:
        answer += (i // k)
    else:
        answer += (i // k) + 1

print(answer)