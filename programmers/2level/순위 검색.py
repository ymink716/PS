from itertools import product

def binary_search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

def solution(info, query):
    candidates = dict()
    for i in info:
        a, b, c, d, e = i.split()
        possible = list(product([a, '-'], [b, '-'], [c, '-'], [d, '-']))
        for p in possible:
            try:
                candidates[''.join(p)].append(int(e))
            except KeyError:
                candidates[''.join(p)] = [int(e)]

    for key in candidates.keys():
        candidates[key].sort()

    answer = []
    for q in query:
        a, b, c, d, e = q.replace(" and ", " ").split()
        k = ''.join([a, b, c, d])
        score = int(e)
        if k not in candidates:
            answer.append(0)
        else:
            answer.append(len(candidates[k]) - binary_search(candidates[k], score))

    return answer


# test case
print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
                ["java and backend and junior and pizza 100",
                 "python and frontend and senior and chicken 200",
                 "cpp and - and senior and pizza 250",
                 "- and backend and senior and - 150",
                 "- and - and - and chicken 100",
                 "- and - and - and - 150"]))

