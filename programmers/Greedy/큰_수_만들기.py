def solution(number, k):
    stack = []  # 자릿수를 담을 스택

    # number의 각 자릿수를 순회하면서
    for n in number:
        # 스택이 비어있지 않고, 현재 자릿수가 스택에서 pop할 값보다 크고, k가 0보다 큰 경우 반복
        while stack and n > stack[-1] and k > 0:
            stack.pop()  # 스택에서 값을 빼준다
            k -= 1  # k를 1 빼준다
        stack.append(n)  # 스택에 자릿수를 채워준다

    # k >0 이라면 아직 제거 횟수를 다 사용하지 않은 경우
    # k 만큼 뒷 부분을 잘라준다
    if k != 0:
        stack = stack[:-k]

    return "".join(stack)


# test
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))