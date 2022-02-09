def solution(n, left, right):
    array = []

    for i in range(left, right + 1):
        s, r = divmod(i, n)
        if s >= r:
            array.append(s + 1)
        else:
            array.append(r + 1)

    return array

# test case
print(solution(3, 2, 5))
print(solution(4, 7, 14))