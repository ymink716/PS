import sys

input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
cities = list(map(int, input().split()))

i, cost = 0, 0  # 현재 도착한 도시의 인덱스, 총 비용
while i < (n - 1):  # 마지막 도시에 도착할 때까지 반복
    d = 0  # i 도시에서 다음 도시까지의 거리
    for j in range(i + 1, n):  # i+1 ~ n 순회
        d += distance[j - 1]  # 다음 도시의 거리 추가
        # 현재 도시에서 주유하는 비용이 더 크면 다음 도시(j)에서 주유하는 것이 이득
        if cities[i] > cities[j]:
            break
    cost += (d * cities[i])
    i = j  # 현재 도시의 위치 변경

print(cost)
