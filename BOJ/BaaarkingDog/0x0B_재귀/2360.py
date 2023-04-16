# 색종이 만들기

n = int(input())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white, blue = 0, 0

def check_square(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 해당 영역 전체 순회하면서
            if color != paper[i][j]:  # 색이 맞지 않으면 4개로 쪼개 재귀 호출
                check_square(x, y, n // 2)
                check_square(x, y + n // 2, n // 2)
                check_square(x + n // 2, y, n // 2)
                check_square(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

check_square(0, 0, n)

print(white)
print(blue)