import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ps = input()
    stack = []
    correct = True
    for p in ps:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0 or stack[-1] == ')':
                correct = False
                break
            else:
                stack.pop()

    if len(stack) == 0 and correct:
        print('YES')
    else:
        print('NO')