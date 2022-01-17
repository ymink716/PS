from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        current = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if current > p:
                break
        answer.append(count)

    return answer

# test
print(solution([1, 2, 3, 2, 3]))