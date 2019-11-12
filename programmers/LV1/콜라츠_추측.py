# 콜라츠 추측
def solution(n):
    for i in range(500):
        if n == 1:
            return i
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return -1


# 테스트
print(solution(6))
print(solution(16))