def solution(n, times):
    # 이분탐색하는 값 : 심사관 1명에게 주어지는 시간
    # high(최악의 경우)는 가장 오래 걸리는 심사관에게 모두 받는 경우
    low, high = 1, max(times) * n

    answer = 0
    while low <= high:
        mid = (low + high) // 2  # 모든 심사관에게 주어진 시간
        people = 0  # 모든 심사관들이 mid분 동안 심사한사람의 수

        # 심사관들의 시간을 순회하면서
        for time in times:
            # 해당 심사관이 주어진 시간 동안 몇 명을 심사할 수 있는지 추가해준다
            people += mid // time

            if people >= n: # mid분 동안 모든 사람을 심사 가능한 경우 -> 시간을 감소
                answer = mid
                high = mid - 1
                break

        if people < n: # mid분 동안 모든 사람을 심사할 수 없는 경우 -> 시간을 증가
            low = mid + 1

    return answer


# test
print(solution(6, [7, 10]))