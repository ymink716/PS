from itertools import combinations
import math

n = int(input())
stat = []
for _ in range(n):
    stat.append(list(map(int, input().split())))

def calculate(a, b, stat):
    x = 0
    for i, j in combinations(a, 2):
        x += stat[i][j] + stat[j][i]
    y = 0
    for i, j in combinations(b, 2):
        y += stat[i][j] + stat[j][i]
    return abs(x - y)

# 조합으로 가능한 팀 생성
team = list(combinations([i for i in range(n)], n // 2))
answer = math.inf
for i in range(len(team) // 2):
    # team[i], team[-i-1]은 서로 겹치지 않음
    answer = min(answer, calculate(team[i], team[-i-1], stat))
print(answer)