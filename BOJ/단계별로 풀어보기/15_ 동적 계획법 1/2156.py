n = int(input())
wines = [0] + [int(input()) for _ in range(n)] + [0]

dp = [0] * (n+2)
dp[1], dp[2] = wines[1], wines[1] + wines[2]

for i in range(3, n+1):
    # 현재 와인을 마시고 바로 전 와인을 건너뜀, 현재 와인을 마시고 바로 전 와인도 마심, 현재 와인을 마시지 않음
    dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i], dp[i-1])

print(dp[n])