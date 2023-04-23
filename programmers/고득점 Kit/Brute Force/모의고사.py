def solution(answers):
    # 수포자들의 찍기 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3  # 수포자들이 맞춘 갯수
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            scores[0] += 1
        if answers[i] == p2[i % len(p2)]:
            scores[1] += 1
        if answers[i] == p3[i % len(p3)]:
            scores[2] += 1

    result = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            result.append(i+1)

    return result


# test
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

