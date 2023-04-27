from itertools import product

def solution(word):
    array = []

    for i in range(1, 6):
        for s in product(['A', 'E', 'I', 'O', 'U'], repeat=i):  # 중복 순열
            array.append(''.join(s))

    array.sort()

    return array.index(word) + 1


# test case
print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))