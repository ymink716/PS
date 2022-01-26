def solution(s):
    answer = ''
    for c in s.split(' '):
        if c == '':
            answer += ' '
        elif c[0].isdigit():
            answer += (c.lower() + ' ')
        else:
            answer += (c[0].upper() + c[1:].lower() + ' ')

    return answer[:-1]  # 마지막 공백 제거

# test
print(solution("3people unFollowed me"))
print(solution("for the last week"))