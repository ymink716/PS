from collections import deque
import sys

input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) == 0:
            print(-1)
            return
        print(self.queue.popleft())

    def size(self):
        print(len(self.queue))

    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)

    def front(self):
        if len(self.queue) == 0:
            print(-1)
            return
        print(self.queue[0])

    def back(self):
        if len(self.queue) == 0:
            print(-1)
            return
        print(self.queue[-1])


q = Queue()

for _ in range(int(input())):
    command = list(input().split())

    if command[0] == "push":
        q.push(command[1])
    elif command[0] == "pop":
        q.pop()
    elif command[0] == "size":
        q.size()
    elif command[0] == "empty":
        q.empty()
    elif command[0] == "front":
        q.front()
    elif command[0] == "back":
        q.back()
