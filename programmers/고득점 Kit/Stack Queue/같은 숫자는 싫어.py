def solution(arr):
    answer = []
    overlap = arr[0] # 현재 1번 이상 나온 숫자
    answer.append(overlap)

    for value in arr[1:]:
        if overlap == value: 
            continue
        overlap = value
        answer.append(overlap)
    return answer


# 테스트
print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
