# 수박수박수박수박수박수?
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)

# 테스트
print(solution(3))
print(solution(4))