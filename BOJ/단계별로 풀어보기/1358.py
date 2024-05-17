import math

w, h, x, y, p = map(int, input().split())
answer = 0

for _ in range(p):
    px, py = map(int, input().split())
    if (
        (x <= px <= x + w and y <= py <= y + h)  # 직사각형 안에 존재하는지
        or math.sqrt(math.pow(x - px, 2) + math.pow((y + h // 2) - py, 2)) <= h // 2  # 왼쪽 원 안에 존재하는지
        or math.sqrt(math.pow((x + w) - px, 2) + math.pow((y + h // 2) - py, 2)) <= h // 2  # 오른쪽 원 안에 존재하는지
    ):
        answer += 1

print(answer)