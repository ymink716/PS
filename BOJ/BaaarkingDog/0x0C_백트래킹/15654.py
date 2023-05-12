# N과 M (5)
# https://www.acmicpc.net/problem/15654

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

answer = []

def back():
    if len(answer) == m:
        print(*answer)

    for num in array:
        if num not in answer:
            answer.append(num)
            back()
            answer.pop()

back()