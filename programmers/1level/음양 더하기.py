def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


# test
print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))