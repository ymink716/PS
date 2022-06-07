import sys

input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    c = input().split()
    if c[0] == 'push':
        stack.append(int(c[1]))
    elif c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])