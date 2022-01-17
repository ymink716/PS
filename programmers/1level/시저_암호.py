# 시저 암호
def solution(s, n):
    result = ""
    for i in s:
        if i.islower():
            result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper():
            result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:
            result += i
    return result
        
            
# 테스트
print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))