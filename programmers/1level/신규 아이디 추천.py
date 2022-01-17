def solution(new_id):
    answer = new_id.lower()  # 1단계

    t1 = ""  # 2단계
    for s in answer:
        if s.isalpha() or s.isnumeric() or s == "-" or s == "_" or s == ".":
            t1 += s
    answer = t1

    t2 = ""  # 3단계
    for i in range(len(answer) - 1):
        if answer[i] == "." and answer[i+1] == ".":
            continue
        t2 += answer[i]
    t2 += answer[-1]
    answer = t2

    # 4단계
    if len(answer) != 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == ".":
        answer = answer[:-1]

    # 5단계
    if answer == "":
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        t3 = answer[-1]
        while len(answer) != 3:
            answer += t3

    return answer


# test
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))