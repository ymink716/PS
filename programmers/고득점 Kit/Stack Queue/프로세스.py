def solution(priorities, location):
    # 큐 초기화 [우선순위, 인덱스]
    q = [[priorities[i], i] for i in range(len(priorities))]

    answer = 0
    while q:  # 큐가 있는 동안 반복
        current = q.pop(0)  # 큐에서 pop
        is_prioritized = True  # pop한 값이 처리될지 판단하기 위한 변수

        # 큐에 남은 요소들을 순회하면서
        for next in q:
            # 현재 pop한 값의 우선순위가 다음 요소들 중 보다 작다면
            if current[0] < next[0]:
                q.append(current)  # 큐의 마지막에 pop한 값을 넣어주고
                is_prioritized = False  # pop한 값은 처리되지 않으므로 False
                break

        # pop한 값이 처리된다면
        if is_prioritized:
            answer += 1  # 인쇄된 횟수 +1
            # 현재 pop한 값의 위치가 찾고자 하는 위치라면
            if current[1] == location:
                return answer


# test
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))