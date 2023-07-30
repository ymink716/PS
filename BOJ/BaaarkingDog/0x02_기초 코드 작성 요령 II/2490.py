# 윷놀이
# https://www.acmicpc.net/problem/2490

for _ in range(3):
    array = list(map(int, input().split()))

    total = sum(array)

    if total == 3:
        print('A')
    elif total == 2:
        print('B')
    elif total == 1:
        print('C')
    elif total == 0:
        print('D')
    elif total == 4:
        print('E')