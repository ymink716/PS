from math import gcd

def solution(arr):
    answer = arr[0]
    # 배열을 순회하면서 이전까지의 최소공배수(answer)와 현재값(arr[i])의 최소공배수를 구해 answer 갱신
    for i in range(1, len(arr)):
        answer = answer * arr[i] // gcd(answer, arr[i])
    return answer


# test case
print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))