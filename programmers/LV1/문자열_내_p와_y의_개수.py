# 문자열 내 p와 y의 개수
def solution(s):
    s = s.upper()
    p_count, y_count = 0, 0
    for str in s:
        if str == 'P':
            p_count += 1
        if str == 'Y':
            y_count += 1
    return p_count == y_count


# 테스트
print(solution("pPoooyY"))
print(solution("Pyy"))