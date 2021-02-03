for _ in range(int(input())):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    h, w, n = map(int, input().split())

    y, x = 0, 0
    if n % h != 0:  # n이 h층으로 나누어 떨어지지 않는 경우
        y = n % h
        x = n // h + 1
    else:  # n이 h층으로 나누어 떨어지는 경우
        y = h
        x = n // h

    if 0 <= x <= 9:
        print(str(y) + '0' + str(x))
    else:
        print(str(y) + str(x))
