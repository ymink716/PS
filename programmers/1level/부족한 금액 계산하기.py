def solution(price, money, count):
    need = 0
    for i in range(1, count + 1):
        need += (price * i)

    if money >= need:
        return 0
    else:
        return need - money


# test
print(solution(3, 20, 4))