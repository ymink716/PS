n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n  # 해당 인덱스를 마지막 원소를 가지는 부분 수열의 최대 길이
for i in range(1, n):  # 1 ~ n-1 순회
    for j in range(i):  # 0 ~ i 순회
        # 해당 원소값(i) > 이전 원소들의 값(j)이면
        # 해당 원소값의 dp와 이전 원소값의 dp +1 중에 최대값으로 업데이트
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))