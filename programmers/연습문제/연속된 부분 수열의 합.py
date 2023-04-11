def solution(sequence, k):
    end = 0
    n = len(sequence)
    result = []
    total = 0

    for start in range(n):
        while total < k and end < n:
            total += sequence[end]
            end += 1

        if total == k:
            result.append([start, end - 1])

        total -= sequence[start]

    result.sort(key=lambda x: (x[1] - x[0], x[0]))

    return result[0]


# test case
print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print((solution([2, 2, 2, 2, 2], 6)))