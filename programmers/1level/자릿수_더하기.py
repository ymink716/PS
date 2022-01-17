# 자릿수 더하기
def solution(n):
    answer = 0
    for value in str(n):
        answer += int(value)
    return answer 


# 테스트
print(solution(123))
print(solution(987))
