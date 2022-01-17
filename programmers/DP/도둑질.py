def solution(money):
    # 동그랗게 연결되어 있으므로 첫 집과 마지막 집이 이웃이라는 점을 고려해야 한다
    # 1. 첫 집을 터는 경우
    f_dp = [money[0], max(money[0], money[1])]

    # 첫 집을 터는 경우 마지막 집을 털지 못하므로 길이-1 까지 순회
    for i in range(2, len(money) - 1):
        f_dp.append(max(money[i] + f_dp[i-2], f_dp[i-1]))

    # 2. 첫 집을 털지 못하는 경우
    l_dp = [0, money[1]]

    for i in range(2, len(money)):
        l_dp.append(max(money[i] + l_dp[i-2], l_dp[i-1]))

    return max(f_dp[-1], l_dp[-1])


# test
print(solution([1, 2, 3, 1]))
print(solution([3, 4, 2, 7, 1]))