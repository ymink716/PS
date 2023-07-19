# 싸이버개강총회
# https://www.acmicpc.net/problem/19583

import sys
input = sys.stdin.readline

def convert_time(t):
    result = 0

    result += int(t[:2]) * 60
    result += int(t[3:])

    return result


s, e, q = input().split()
s, e, q = convert_time(s), convert_time(e), convert_time(q)

entrance, exit = set(), set()

while True:
    try:
        time, name = input().split()
        time = convert_time(time)

        if time <= s:  # 입장 여부 확인
            entrance.add(name)
        elif e <= time <= q:  # 퇴장 여부 확인
            exit.add(name)
    except ValueError:
        break

# 입장 회원, 퇴장 회원의 교집합
print(len(entrance.intersection(exit)))