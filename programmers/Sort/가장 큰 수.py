from functools import cmp_to_key

def compare(x, y):
    a = int(str(x) + str(y))  # 앞뒤 값을 결합
    b = int(str(y) + str(x))  # 앞뒤 값을 바꿔서 결합

    if a > b:  # x가 앞에 온다
        return -1
    elif a < b:  # y가 앞에 온다
        return 1
    else:  # 그대로
        return 0


def solution(numbers):
    numbers.sort(key=cmp_to_key(compare))
    answer = "".join(map(str, numbers))
    return answer if answer[0] != '0' else '0'


# test case
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))