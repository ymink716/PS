# 하샤드 수
def solution(x):
    total = sum(map(int, str(x)))
    return x % total == 0


# 테스트
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))