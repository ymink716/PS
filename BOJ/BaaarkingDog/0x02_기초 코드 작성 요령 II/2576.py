# 홀수
# https://www.acmicpc.net/problem/2576

total = 0
min_value = 101

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        total += n
        min_value = min(min_value, n)

if total == 0:
    print(-1)
else:
    print(total)
    print(min_value)