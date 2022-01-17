from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:  # 각 코스의 개수를 순회
        temp = []
        for order in orders:  # 각 손님의 주문을 순회
            # 주문건에 대해 코스의 개수 만큼 조합 (순서 때문에 정렬)
            comb = combinations(sorted(order), c)
            temp += comb  # 구한 조합들을 temp 배열에 담아준다
        counter = Counter(temp)  # Counter 객체로 변환
        # 카운터가 비어 있지 않고 최대값이 2 이상이라면
        if len(counter) != 0 and max(counter.values()) >= 2:
            # couter 객체에서 최대값을 가진 요소들을 모두 더해줌
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)  # 오름차순으로 정렬해서 리턴



# test
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
#print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))