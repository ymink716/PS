# 정수 제곱근 판별
def solution(n):
    if int(n ** 0.5) ** 2 == n:
        return (int(n ** 0.5) + 1) ** 2
    return -1


# 테스트
print(solution(121))
print(solution(3))