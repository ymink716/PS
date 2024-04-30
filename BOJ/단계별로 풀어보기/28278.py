import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack.pop())

    def print_length(self):
        print(len(self.stack))

    def is_empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)

    def print_top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])

stack = Stack()

for _ in range(int(input())):
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack.push(command[1])
    elif command[0] == 2:
        stack.pop()
    elif command[0] == 3:
        stack.print_length()
    elif command[0] == 4:
        stack.is_empty()
    elif command[0] == 5:
        stack.print_top()