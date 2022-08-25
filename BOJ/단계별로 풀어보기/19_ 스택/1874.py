n = int(input())
stack = []
op = []
current = 1
possible = True

for _ in range(n):
    num = int(input())
    while current <= num:  # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(current)
        op.append('+')
        current += 1

    if stack[-1] == num:  # stack의 top이 입력한 숫자와 같다면 값을 꺼내 수열을 만든다
        stack.pop()
        op.append('-')
    else:  # 그게 아니면 수열을 만들 수 없음
        possible = False

if not possible:
    print('NO')
else:
    for i in op:
        print(i)