# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    # 정렬로 비교할 요소가 여러 개이면 튜플로 그 순서를 보내줌
    # n번째 인덱스 문자 순, 전체 문자열 순
    return sorted(strings, key = lambda str : (str[n], str))

# 테스트
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))