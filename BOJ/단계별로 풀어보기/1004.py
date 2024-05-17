import math

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())  # 출발점, 도착점
    n = int(input())
    answer = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())  # 행성의 중점, 반지름
        temp = 0
        # 현재 행성의 중점과 출발점 사이의 거리 < 반지름
        if math.sqrt(math.pow(cx - x1, 2) + math.pow(cy - y1, 2)) < r:
            temp += 1
        # 현재 행성의 중점과 도착점 사이의 거리 < 반지름
        if math.sqrt(math.pow(cx - x2, 2) + math.pow(cy - y2, 2)) < r:
            temp += 1
        # 현재 행성이 출발점과 도착점 중 하나만 포함하고 있어야 진입/이탈
        if temp == 1:
            answer += 1
    print(answer)