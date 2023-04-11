# N번째 큰 수

import heapq

pq = []
n = int(input())

# 우선순위 큐 값을 첫번째 줄로 초기화
for number in map(int, input().split()):
    heapq.heappush(pq, number)

# 두번째 줄 ~ n번째 줄 까지 순회
for _ in range(n - 1):
    # 우선순위 큐에 해당 줄의 숫자들을 넣어줌
    for number in map(int, input().split()):
        heapq.heappush(pq, number)
    # 현재 2n개 만큼 값이 들어있는데 여기서 n개를 pop()하면 큰 수 n개만 남음 (최소힙)
    for _ in range(n):
        heapq.heappop(pq)

print(min(pq))  # 남은 숫자들 중에 최소값이 n번째 큰 수