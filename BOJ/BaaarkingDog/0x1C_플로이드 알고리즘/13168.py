# 내일로 여행
# https://www.acmicpc.net/problem/13168

import sys
input = sys.stdin.readline

n, r = map(int, input().split())
cities = set(input().split())

n = len(cities)
c_index = {city: i for i, city in enumerate(cities)}  # 도시 별 인덱스 지정

m = int(input())
plans = list(map(lambda x: c_index[x], input().split()))  # 방문해야 하는 도시를 인덱스로 바꿔서 저장

# 내일로 티켓 x, 내일로 티켓 o 그래프 초기화
normal = [[1e9] * n for _ in range(n)]
railro = [[1e9] * n for _ in range(n)]

# 여행 경로 입력 받아 s -> e 로 가는 더 적은 비용 구하기
for _ in range(int(input())):
    t, s, e, c = input().split()
    s = c_index[s]
    e = c_index[e]
    c = int(c)

    # 내일로 티켓 x
    normal[s][e] = min(normal[s][e], c)
    normal[e][s] = min(normal[e][s], c)

    # 내일로 티켓 o
    if t in ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun']:  # 무료
        railro[s][e] = 0
        railro[e][s] = 0
    elif t in ['S-Train', 'V-Train']:  # 50%
        railro[s][e] = min(railro[s][e], c / 2)
        railro[e][s] = min(railro[e][s], c / 2)
    else:
        railro[s][e] = min(railro[s][e], c)
        railro[e][s] = min(railro[e][s], c)

# 플로이드 워셜 알고리즘 수행
for k in range(n):
    for i in range(n):
        for j in range(n):
            normal[i][j] = min(normal[i][j], normal[i][k] + normal[k][j])
            railro[i][j] = min(railro[i][j], railro[i][k] + railro[k][j])

normal_cost, railro_cost = 0, 0
for i in range(m - 1):  # 방문 계획에 따른 비용 계산
    normal_cost += normal[plans[i]][plans[i + 1]]
    railro_cost += railro[plans[i]][plans[i + 1]]

if railro_cost + r < normal_cost:
    print('Yes')
else:
    print('No')