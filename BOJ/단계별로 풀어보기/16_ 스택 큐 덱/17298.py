from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

stack = deque()
answer = [-1 for _ in range(n)]

# array를 앞에서부터 순회하면서
for i in range(n):
    # stack이 비어 있지 않고, stack의 top이 현재값(array[i])보다 작다면
    while stack and stack[-1][0] < array[i]:
        _, index = stack.pop()  # 스택에서 pop
        answer[index] = array[i]  # 오큰수 변경
    # stack에 현재 array[i] 값과 인덱스를 넣어줌
    stack.append([array[i], i])

for num in answer:
    print(num, end=" ")