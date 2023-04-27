def solution(name):
    answer = 0  # 조이스틱 조작 횟수
    min_move = len(name) - 1  # 기본 최소 좌우 이동 횟수 : 길이 - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값을 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존값, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽 시작 방식 비교
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))

    answer += min_move  # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    return answer

"""
참고 : https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy#%EC%B6%94%EA%B0%80-%EC%84%A4%EB%AA%85
"""

# test
print(solution('JEROEN'))
print(solution('JAN'))