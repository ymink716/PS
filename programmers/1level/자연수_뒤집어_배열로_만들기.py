# 자연수 뒤집어 배열로 만들기
def solution(n):
    arr = list(str(n))
    answer = []
    for i in reversed(arr):
        answer.append(int(i))
    return answer


# 테스트
print(solution(12345))