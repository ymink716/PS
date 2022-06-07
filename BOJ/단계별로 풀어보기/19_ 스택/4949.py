while True:
    s = input()

    if s == '.':
        break

    stack = []
    correct = True
    for i in s:
        if i in ['[', '(']:
            stack.append(i)
        elif i in [']', ')']:
            if len(stack) == 0 or (stack[-1] == '(' and i == ']') or (stack[-1] == '[' and i == ')'):
                correct = False
                break
            else:
                stack.pop()

    if len(stack) == 0 and correct:
        print('yes')
    else:
        print('no')