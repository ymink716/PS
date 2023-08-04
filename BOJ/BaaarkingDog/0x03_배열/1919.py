# 애너그램 만들기
# https://www.acmicpc.net/problem/1919

from collections import defaultdict

d = defaultdict(int)

for i in input():
    d[i] += 1

for i in input():
    d[i] -= 1

answer = 0
for i in d.values():
    if i != 0:
        answer += abs(i)

print(answer)