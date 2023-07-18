# 암호 만들기
# https://www.acmicpc.net/problem/1759

l, c = map(int, input().split())
array = list(input().split())

array.sort()  # 오름차순 정렬
answer = []

def back(start):
    if len(answer) == l:
        a, b = 0, 0  # 모음 개수, 자음 개수
        for s in answer:
            if s in ['a', 'e', 'i', 'o', 'u']:
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            print(''.join(answer))
        return

    for i in range(start, c):
        answer.append(array[i])
        back(i + 1)
        answer.pop()

back(0)