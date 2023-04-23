def solution(bridge_length, weight, truck_weights):
    time = 0  # 경과 시간
    on_bridge = [0] * bridge_length  # 다리 위에 있는 트럭 리스트 초기화
    weight_sum = 0  # 다리 위 무게 합

    while on_bridge:
        time += 1  # 1초 경과
        weight_sum -= on_bridge.pop(0)  # 다리 위 리스트 맨 앞 요소 제거

        if truck_weights:  # 대기 중인 트럭이 존재한다면
            # (현재 다리 위 무게 합 + 다리에 진입할 트럭의 무게)가 다리가 견딜 수 있는 weight라면
            if weight_sum + truck_weights[0] <= weight:
                weight_sum += truck_weights[0]  # 다리 위 무게 합에 해당 트럭 추가
                on_bridge.append(truck_weights.pop(0))  # 다리 위에 있는 트럭 리스트에 추가
            # 그게 아니라면 0을 추가
            else:
                on_bridge.append(0)

    return time


#test
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
