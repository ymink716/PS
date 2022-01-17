def solution(numbers):
    s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s2 = set(numbers)

    return sum(s1 - s2)


# test
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))