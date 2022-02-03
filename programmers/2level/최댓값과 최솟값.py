def solution(s):
    array = list(map(int, s.split()))
    return "{0} {1}".format(min(array), max(array))

#test case
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))