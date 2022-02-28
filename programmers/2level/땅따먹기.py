def solution(land):
    # 1행부터 마지막 행까지 순회
    for i in range(1, len(land)):
        # land[i][j]의 값을 이전 행에서 열이 겹치지 않는 것들 중 최대값을 더해 갱신
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])


# test case
print(solution([[1, 2, 3, 5],
                [5, 6, 7, 8],
                [4, 3, 2, 1]]))