def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance  # 거리의 최소값, 최대값
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 기준값 : 바위 사이의 최소 거리
        prev = 0  # 기준이 되는 돌
        removed = 0  # 제거한 돌의 개수

        # 각 돌을 돌면서 제거할 돌을 찾는다
        for rock in rocks:
            if rock - prev < mid:  # 돌 사이의 거리가 기준값보다 작으면 제거
                removed += 1
            else:  # 아니라면 현재 돌을 새 기준으로
                prev = rock
            if removed > n:  # 제거된 돌이 문제 조건보다 크면 break
                break

        if removed > n:  # 제거된 돌이 더 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽을 줄인다.
            right = mid - 1
        else:  # 반대라면 큰 쪽으로 줄인다
            left = mid + 1
            answer = mid

    return answer


# test
print(solution(25, [2, 14, 11, 21, 17], 2))