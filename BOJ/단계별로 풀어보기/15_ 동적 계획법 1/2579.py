n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
else:
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, n + 1):
        # i의 최대 점수 = max(i-1의 점수 + i-3까지의 최대 점수, i-2까지의 최대점수) + i의 점수
        dp[i] = max(stairs[i-1] + dp[i-3], dp[i-2]) + stairs[i]
    print(dp[n])