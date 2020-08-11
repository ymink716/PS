import math

N = int(input())

for i in range(N):
    k, n = list(map(int, input().split(' ')))
    numerator, denominator = 1, 1  # 분자, 분모

    # 조합의 개수 구하기
    for j in range(1, k+1):
        numerator *= n + 1 - j
        denominator *= j
    print(numerator // denominator)