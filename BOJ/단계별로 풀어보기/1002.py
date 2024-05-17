import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 두 터렛의 거리

    # 두 원이 일치하는 경우
    if distance == 0 and r1 == r2:
        print(-1)
    # 두 원이 한 점에서 만나는 경우 (외접 or 내접)
    elif distance == (r1 + r2) or abs(r1 - r2) == distance:
        print(1)
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)
