# 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847

n = int(input())

scores = []
for _ in range(n):
    scores.append(int(input()))

answer = 0
# 뒤에서 부터 순회
for i in range(n - 1, 0, -1):
    # i -1 점수 >= i 점수
    if scores[i - 1] >= scores[i]:
        cnt = scores[i - 1] - scores[i] + 1  # 이 구간에서 감소 횟수
        scores[i - 1] -= cnt  # i -1 점수를 cnt 만큼 감소
        answer += cnt

print(answer)