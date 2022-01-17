def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b % 1000000007


# test
print(solution(4))

# 1 : 1
# 2 : 11 / 2
# 3 : 111 / 21 / 12
# 4 : 1111 / 112 / 121 / 211 / 22