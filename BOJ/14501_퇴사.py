N = int(input())

day_list = []
pay_list = []
dp = []

for i in range(N):
    day, pay = map(int, input().split())
    day_list.append(day)
    pay_list.append(pay)
    dp.append(pay)

dp.append(0)
for i in range(N-1, -1, -1):
    if day_list[i] + i > n:


print(dp[0])


