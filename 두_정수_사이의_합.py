# 두 정수 사이의 합
def solution(a, b):
    lst = []
    if a == b:
        return a
    for i in range(min(a, b), max(a, b)+1):
        lst.append(i)
    return sum(lst)


# 테스트
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
