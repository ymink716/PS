# N과 M (6)
# https://www.acmicpc.net/problem/15655

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()  # 오름차순으로 정렬
answer = []

def back(start, count):
    if count == m:  # answer 리스트에 담긴 숫자의 갯수가 m개면 출력
        print(*answer)
        return

    for i in range(start, n):  # 오름차순 정렬되어 있으므로 start부터
        if array[i] not in answer:
            answer.append(array[i])
            back(i, count + 1)
            answer.pop()

back(0, 0)