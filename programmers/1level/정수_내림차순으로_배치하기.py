# 정수 내림차순으로 배치하기
def solution(n):
    arr = sorted(list(str(n)), reverse=True)
    return int(''.join(arr))


# 테스트
print(solution(118372))