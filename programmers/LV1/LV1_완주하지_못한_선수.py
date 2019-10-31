# 완주하지 못한 선수

# Counter 객체로 변환
# 완주하지 못한 사람은 1명이므로 두 Counter 객체를 빼주면 {'사람': 1} 형태의 값이 나온다
# keys()로 키를 받고 list로 변환한 후 0번째 인덱스에 접근하면 정답을 구할 수 있다

from collections import Counter

def solution(p, c):
    p_count = Counter(p)
    c_count = Counter(c)
    return list((p_count - c_count).keys())[0]