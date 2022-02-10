def solution(s):
    answer = 0
    # 0부터 s의 길이까지 순회하면서 괄호 검사
    for x in range(len(s)):
        stack = []
        check = True
        for i in s:
            # 여는 괄호인 경우
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            # 닫는 괄호인 경우
            else:
                if len(stack) == 0: 
                    check = False
                    break
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
        if check and len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]
    return answer


# tset case
print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))