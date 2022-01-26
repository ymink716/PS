def solution(n):
    answer = 1  # n 하나로 이루어진 경우의 수 추가
    # 1 ~ n의 절반까지 순회하면서
    for i in range(1, n // 2 + 1):
        num, total = i, 0
        # i부터 연속한 자연수들의 합(total)을 구함 (n보다 크거나 같아질 때까지)
        while total < n:
            total += num
            num += 1
        if total == n:  # 연속한 자연수들의 합 = n인 경우 answer +1
            answer += 1
    return answer


# test
print(solution(15))