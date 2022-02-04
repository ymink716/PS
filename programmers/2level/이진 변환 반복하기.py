def solution(s):
    answer = [0, 0]

    # s가 "1"이 될 때까지 반복
    while s != "1":
        cnt = s.count("0")  # 문자열 s에서 0의 개수
        answer[1] += cnt  # 제거된 0의 개수 추가
        c = len(s) - cnt  # 0을 제거한 s의 길이
        answer[0] += 1  # 변환 횟수 추가
        s = bin(c)[2:]  # c를 2진법으로 표현한 문자열로 s 재정의 

    return answer


# test case
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))