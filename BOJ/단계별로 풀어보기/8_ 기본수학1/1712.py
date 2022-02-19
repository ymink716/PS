a, b, c = map(int, input().split())  # 고정비, 가변비, 판매가

if b >= c:
    print(-1)
else:
    r = c - b  # 순이익
    answer = a // r + 1
    print(answer)

