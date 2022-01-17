def solution(lottos, win_nums):
    answer = []

    correct = 0
    zeros = 0
    for n in lottos:
        if n in win_nums:
            correct += 1
        elif n == 0:
            zeros += 1

    max_num, min_num = correct + zeros, correct

    if max_num < 2:
        answer.append(6)
    else:
        answer.append(7 - max_num)

    if min_num < 2:
        answer.append(6)
    else:
        answer.append(7 - min_num)

    return answer


# test
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))