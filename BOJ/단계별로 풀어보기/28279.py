from collections import deque
import sys

input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.deque = deque()

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if len(self.deque) == 0:
            print(-1)
            return
        print(self.deque.popleft())

    def pop_back(self):
        if len(self.deque) == 0:
            print(-1)
            return
        print(self.deque.pop())

    def print_length(self):
        print(len(self.deque))

    def is_empty(self):
        if len(self.deque) == 0:
            print(1)
        else:
            print(0)

    def is_empty(self):
        if len(self.deque) == 0:
            print(1)
        else:
            print(0)

    def print_front(self):
        if len(self.deque) == 0:
            print(-1)
            return
        print(self.deque[0])

    def print_back(self):
        if len(self.deque) == 0:
            print(-1)
            return
        print(self.deque[-1])

d = Deque()

for _ in range(int(input())):
    command = list(map(int, input().split()))

    if command[0] == 1:
        d.push_front(command[1])
    elif command[0] == 2:
        d.push_back(command[1])
    elif command[0] == 3:
        d.pop_front()
    elif command[0] == 4:
        d.pop_back()
    elif command[0] == 5:
        d.print_length()
    elif command[0] == 6:
        d.is_empty()
    elif command[0] == 7:
        d.print_front()
    elif command[0] == 8:
        d.print_back()
