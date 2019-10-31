# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for value in arr:
        if value % divisor == 0:
            answer.append(value)
    answer.sort()
    return answer if len(answer) != 0 else [-1]

# 테스트
print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))