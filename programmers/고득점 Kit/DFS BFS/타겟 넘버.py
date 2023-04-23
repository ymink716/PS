def solution(numbers, target):
    p_list = [0]  # 부모 노드 리스트

    for num in numbers:
        c_list = []   # 자식 노드 리스트
        # 부모 노드에 num을 더하고 빼준 것을 자식 노드에 추가
        for v in p_list:
            c_list.append(v + num)
            c_list.append(v - num)
        p_list = c_list   # 자식노드 -> 부모노드

    return p_list.count(target)  # 모든 연산이 끝난 리스트에서 target 값을 count


# test
print(solution([1, 1, 1, 1, 1], 3))

"""
# 다른 풀이
answer = 0

def dfs(i, numbers, target, value):
    global answer
    N = len(numbers)
    # i == N : 마지막 연산까지 끝낸 상태
    # target == value라면 answer += 1
    if (i == N and target == value):
        answer += 1
        return
    if (i == N):
        return
    
    # 재귀를 통해 다음 숫자의 연산 진행 (+, -)
    dfs(i + 1, numbers, target, value + numbers[i])
    dfs(i + 1, numbers, target, value - numbers[i])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer
"""