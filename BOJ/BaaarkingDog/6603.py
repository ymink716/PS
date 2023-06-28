# 로또
# https://www.acmicpc.net/problem/6603

while True:
    array = list(map(int, input().split()))
    k = array[0]

    if k == 0:  # 종료 조건
        break

    s = array[1:]
    answer = []

    def back(start, cnt):
        if cnt == 6:
            print(*answer)
            return

        for i in range(start, k):
            if s[i] not in answer:
                answer.append(s[i])
                back(i + 1, cnt + 1)
                answer.pop()

    back(0, 0)
    print()