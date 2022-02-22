from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        count = 0
        now = k
        for d in p:
            if now >= d[0]:
                now -= d[1]
                count += 1
        if count > answer:
            answer = count

    return answer


# test case
print(solution(80, [[80, 20], [50, 40], [30, 10]]))
