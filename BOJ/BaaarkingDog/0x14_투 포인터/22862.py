# 가장 긴 짝수 연속한 부분 수열 (large)
# https://www.acmicpc.net/problem/22862

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))

result = 0  # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이
count = 0  # 지워진 홀수 카운트
end = 0
temp = 0  # 현재 투 포인터만큼의 짝수 부분 수열의 길이

for start in range(N):  # start를 N까지 증가시키면서
    # 홀수를 지울 수 있는 기회가 남아있음 and end를 끝점까지가는 동안 반복
    while count <= K and end < N:
        if array[end] % 2 == 1:  # 홀수
            count += 1
        else:  # 짝수
            temp += 1
        end += 1  # 끝 점 이동

        if start == 0 and end == N:  # K가 남았는데도 end가 N까지 간 경우
            result = temp
            break

    if count == K + 1:  # 더 이상 지울 수 없게 되었을 때
        result = max(temp, result)  # result 갱신

    # start 값 변경 전에
    if array[start] % 2 == 1:  # 시작점이 홀수
        count -= 1
    else:  # 시작점이 짝수
        temp -= 1

print(result)