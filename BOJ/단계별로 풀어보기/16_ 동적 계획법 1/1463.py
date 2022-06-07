n = int(input())

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1  # 1을 뺀 경우 : i-1의 최소값에 +1
    if i % 3 == 0:  # 3으로 나누어 떨어진다면 1을 뺀 경우와 i//3의 결과값 +1 중에 최소값으로
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:  # 2로 나누어 떨어진다면 현재 dp값과 i//2의 결과값 +1 중에 최소값으로
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])

