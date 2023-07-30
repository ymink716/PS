# 카드 역배치
# https://www.acmicpc.net/problem/10804

array = [0] + [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())

    for i in range((b - a) // 2 + 1):
        array[a + i], array[b - i] = array[b - i], array[a + i]

print(*array[1:])