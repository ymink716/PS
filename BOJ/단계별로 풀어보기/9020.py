import math

max_value = 10000
array = [True for _ in range(max_value + 1)]

# n의 최대값까지 소수 판별
for i in range(2, int(math.sqrt(max_value)) + 1):
    if array[i]:
        j = 2
        while i * j <= max_value:
            array[i * j] = False
            j += 1

for _ in range(int(input())):
    n = int(input())
    # 두 소수의 차이가 가장 적은 것이 우선하므로 n의 절반부터 시작
    for i in range(n // 2, 1, -1):
        # i, n - 1 둘 다 소수이면 출력
        if array[i] and array[n - i]:
            print(i, n - i)
            break