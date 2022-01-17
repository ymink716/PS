def solution(people, limit):
    # people을 내림차순을 Sort
    people.sort(reverse=True)

    # 현재 가장 무거운 사람, 현재 가장 가벼운 사람
    start, end = 0, len(people) - 1

    # 시작점이 끝점보다 작을 때까지 반복
    while start <= end:
        # 남아있는 가장 무거운 사람 + 가장 가벼운 사람 <= limit : 같이 탈출
        # 그게 아니면 가장 무거운 사람만 혼자 탈출
        if people[start] + people[end] <= limit:
            end -= 1  # 가장 가벼운 사람 탈출
        start += 1  # 가장 무거운 사람 탈출

    # start 값이 사람들이 나간 횟수
    return start


# test
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))