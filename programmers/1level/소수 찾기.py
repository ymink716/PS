import math

def solution(n):
    array = [1 for _ in range(n + 1)]
    array[0], array[1] = 0, 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == 1:
            j = 2
            while i * j <= n:
                array[i * j] = 0
                j += 1

    return sum(array)


# test
print(solution(10))
print(solution(5))