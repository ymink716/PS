# 피보나치 함수
# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [(1, 0), (0, 1)]  # (f(0) 호출 횟수, f(1) 호출횟수)

    for i in range(2, n + 1):
        # f(n)의 f(0), f(1)의 호출 횟수 = f(n-1) ~ + f(n-2) ~
        dp.append((dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]))

    print(dp[n][0], dp[n][1])