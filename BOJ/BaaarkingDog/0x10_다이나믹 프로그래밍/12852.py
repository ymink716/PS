# 1로 만들기 2
# https://www.acmicpc.net/problem/12852

n = int(input())

# [x를 만드는 최소 연산의 수, [만드는 방법에 대한 기록]]
dp = [[0, []] for _ in range(n + 1)]
# f(1) 초기화
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n + 1):
    # 현재 수에서 1을 빼는 경우로 dp[i] 채우기
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]

    # 현재 수가 2로 나누어 떨어지고, f(x // 2) + 1 이 더 작다면 변경
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

    # 현재 수가 3로 나누어 떨어지고,  f(x // 3) + 1 이 더 작다면 변경
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]

print(dp[n][0])  # 연산의 최소값 출력
for i in dp[n][1][::-1]:  # 역순으로 기록 출력
    print(i, end=' ')