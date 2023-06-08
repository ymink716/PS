# 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)  # 다리 위 무게를 저장할 리스트
time = 0

while bridge:  # 다리의 모든 트럭이 지나갈 동안 반복
    time += 1  # 시간 단위 증가
    bridge.popleft()  # 다리의 맨 앞 칸 제거

    if trucks:  # 대기 중인 트럭이 남아있다면
        if sum(bridge) + trucks[0] <= l:  # 다리 위 무게의 합 + 진입할 트럭 <= 다리의 최대하중
            bridge.append(trucks.popleft())  # 트럭 진입
        else:  # 트럭이 진입 못하는 경우
            bridge.append(0)  # 다리의 공간을 채우기 위해 0 push

print(time)
