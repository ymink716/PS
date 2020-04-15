# 예산
def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0: return i
    return len(d)


# 테스트
print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))