def solution(s):
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0


# test
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))