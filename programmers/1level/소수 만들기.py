import math
import itertools

def solution(nums):
    n = 3000
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    answer = 0
    for x in itertools.combinations(nums, 3):
        if array[sum(x)]:
            answer += 1

    return answer


# test
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))