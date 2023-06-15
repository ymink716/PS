# 주식
# https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))

    answer = 0
    max_price = array[-1]  # 주식의 최대값을 마지막 날의 가격으로
    for i in range(n - 2, -1, -1):  # 뒤에서부터 거꾸로 순회
        if array[i] < max_price:  # 해당 날의 주식이 최대 가격보다 작으면
            answer += max_price - array[i]  # 이익 += 최대가격 - 해당 날 가격
        elif array[i] > max_price:  # 해당 날의 주식이 최대 가격보다 크면
            max_price = array[i]  # 최대 가격 갱신

    print(answer)