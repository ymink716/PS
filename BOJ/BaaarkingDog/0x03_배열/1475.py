# 방 번호
# https://www.acmicpc.net/problem/1475

n = input()
array = [0] * 9

for s in n:
    if s == '9':
        array[6] += 1
    else:
        array[int(s)] += 1

if array[6] % 2 == 1:
    array[6] = array[6] // 2 + 1
else:
    array[6] = array[6] // 2

print(max(array))