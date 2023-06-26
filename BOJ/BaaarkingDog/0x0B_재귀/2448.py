# 별 찍기 - 11
# https://www.acmicpc.net/problem/2448

n = int(input())

def draw_star(n):
    if n == 3:
        return [
            '  *  ',
            ' * * ',
            '*****'
        ]

    arr = draw_star(n // 2)
    stars = []

    # 위쪽 삼각형 가운데로 오게 하기 위해 양 옆에 n//2 만큼 공백 추가
    for i in arr:
        stars.append(' ' * (n // 2) + i + ' ' * (n // 2))

    # 왼쪽, 오른쪽 아래 삼각형 -> 가운데 공백 하나 추가해서 합치기
    for i in arr:
        stars.append(i + ' ' + i)

    return stars

stars = draw_star(n)

for s in stars:
    print(s)