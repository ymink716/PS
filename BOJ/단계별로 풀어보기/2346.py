from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
answer = []


while q:
    i, next = q.popleft()
    answer.append(i + 1)

    if next > 0:
        q.rotate(-(next - 1))
    else:
        q.rotate(-next)

print(' '.join(map(str, answer)))