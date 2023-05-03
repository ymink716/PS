# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

for _ in range(int(input())):
    d = dict()
    n = int(input())

    for i in range(n):  # (category, 개수)
        name, category = input().split()
        if category in d:
            d[category] += 1
        else:
            d[category] = 1

    # (a + 1) * (b + 1) ... - 1
    # (a의 옷의 개수 + 안 입는 경우) + (b의 옷의 개수 + 안입는 경우)... - 다 안입는 경우
    result = 1
    for v in d.values():
        result = result * (v + 1)
    print(result - 1)


