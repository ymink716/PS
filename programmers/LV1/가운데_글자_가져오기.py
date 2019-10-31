# 가운데 글자 가져오기
def solution(s):
    index = int(len(s) / 2) # 가운데 인덱스
    if len(s) % 2 == 0: # 글자수가 짝수인 경우
        return s[index-1:index+1]
    else: # 홀수인 경우
        return s[index] 


# 테스트
print(solution("abcde"))
print(solution("qwer"))