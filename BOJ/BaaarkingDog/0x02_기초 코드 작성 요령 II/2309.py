# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

array = []
for _ in range(9):
    array.append(int(input()))

array.sort()
total = sum(array)

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if total - array[i] - array[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(array[k])
            exit(0)