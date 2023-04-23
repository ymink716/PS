def solution(n, results):
    # key: n번째 선수, value : n번 선수가 이긴/이기지 못한 사람들의 집합
    win, lose = {}, {}
    for i in range(1, n+1):
        win[i], lose[i] = set(), set()

    # 경기 결과에 대해 반복문을 돌면서 win, lose에 이긴 경우와 진 경우를 담는다
    for a, b in results:
        win[a].add(b)   # a가 b를 이김
        lose[b].add(a)   # b는 a에게 짐

    # 전체 선수들을 순회하면서
    for i in range(1, n+1):
        # i를 이긴 사람들(winner)은 i에게 진 사람(win[i])은 반드시 이긴다
        for winner in lose[i]:
            win[winner].update(win[i])  # set의 update는 여러 값을 한번에 추가

        # i에게 진 사람들(loser)은 i를 이긴 사람들(lose[i])에게는 반드시 진다
        for loser in win[i]:
            lose[loser].update((lose[i]))

    # i번 선수가 이긴 사람의 수와 진 사람의 수를 합쳐 n-1이 되면 순위를 구할 수 있다
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer


# test
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))