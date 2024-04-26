from collections import deque

n = int(input())
queue = deque(map(int, input().split()))

stack = []
now = 1

while queue:
    if queue[0] == now:
        queue.popleft()
        now += 1
    else:
        stack.append(queue.popleft())

    while stack and stack[-1] == now:
        stack.pop()
        now += 1

if stack:
    print("Sad")
else:
    print("Nice")


