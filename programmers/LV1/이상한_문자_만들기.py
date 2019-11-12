# 이상한 문자 만들기
def solution(s):
    answer = ""
    index = 0
    for char in s:
        if char == " ":
            answer += " "
            index = 0
            continue
        if index % 2 == 0:
            answer += char.upper()
        else: 
            answer += char.lower()
        index += 1
    return answer


print(solution("try hello world"))