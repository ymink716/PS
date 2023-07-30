# 핸드폰 요금
# https://www.acmicpc.net/problem/1267

n = int(input())
array = list(map(int, input().split()))

y_cost, m_cost = 0, 0

for time in array:
    y_cost += (time // 30 + 1) * 10
    m_cost += (time // 60 + 1) * 15

if y_cost < m_cost:
    print('Y', y_cost)
elif y_cost > m_cost:
    print('M', m_cost)
else:
    print('Y M', y_cost)