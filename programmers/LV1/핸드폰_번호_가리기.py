# 핸드폰 번호 가리기
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[len(phone_number) - 4:]


# 테스트
print(solution("01033334444"))
print(solution("027778888"))