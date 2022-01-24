def solution(A, B):
    x = 0
    A.sort(), B.sort(reverse=True)
    for i in range(len(A)):
        x += (A[i] * B[i])

    y = 0
    A.sort(reverse=True), B.sort()
    for i in range(len(A)):
        y += (A[i] * B[i])

    return max(x, y)


# test
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))