# 걸그룹 마스터 준석이
# https://www.acmicpc.net/problem/16165

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = dict()

for _ in range(n):
    team = input().rstrip()
    d[team] = []
    for _ in range(int(input())):
        d[team].append(input().rstrip())

for _ in range(m):
    name = input().rstrip()
    type = int(input().rstrip())

    if type == 0:  # 해당 팀에 속한 멤버들 사전순으로 출력
        for member in sorted(d[name]):
            print(member)
    else:  # 해당 멤버가 속한 팀의 이름 출력
        for team in d:
            if name in d[team]:
                print(team)
                break