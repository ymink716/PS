# 문자열 다루기 기본
def solution(s):
    if len(s) not in [4, 6]:
        return False
    return s.isdigit()

# 테스트    
print(solution("a234"))
print(solution("1234"))