def draw_star(n, stars):
    if n == 3:
        return stars
    array = []  # 별을 담을 리스트
    for i in stars:  # 위에 3개의 구역
        array.append(i * 3)
    for i in stars:  # 가운데 3개의 구역 (중앙이 비어있음)
        array.append(i + ' ' * len(stars) + i)
    for i in stars:  # 아래 3개의 구역
        array.append(i * 3)
    return draw_star(n // 3, array)

n = int(input())
first = ["***", "* *", "***"]
result = draw_star(n, first)
for i in result:
    print(i)
