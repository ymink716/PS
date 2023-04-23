def solution(clothes):
    d = {}  # {옷의 종류 : 개수}를 담을 딕셔너리

    for c in clothes:
        if c[1] in d:
            d[c[1]] += 1
        else:
            d[c[1]] = 1

    # 경우의 수 :
    # 각 카테고리의 개수 + 1 을 전부 곱한 후 1을 빼준다
    # (a + 1) * (b + 1) * (c + 1) *... - 1
    # +1 은 해당 카테고리가 선택되지 않은 경우
    # -1 은 모든 카테고리에서 선택되지 않은 경우를 제외하기 위한 것
    answer = 1
    for key in d.keys():
        answer *= d[key] + 1

    return answer - 1


# test
print(solution([["yellow_hat", "headgear"],
                 ["blue_sunglasses", "eyewear"],
                 ["green_turban", "headgear"]]))

print(solution([["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))