# 숫자
# https://www.acmicpc.net/problem/10093

a, b = map(int, input().split())

if a > b:
    a, b = b, a
elif a == b:
    print(0)
    exit(0)

print(b - a - 1)

for i in range(a + 1, b):
    print(i, end=" ")