# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447


def draw_star(n):
    if n == 1:
        return "*"

    # n의 별찍기는 n //3 의 별찍기 결과가 필요 -> 재귀
    stars = draw_star(n // 3)
    result = []

    for s in stars:
        result.append(s * 3)
    for s in stars:  # 공백이 있는 라인 처리
        result.append(s + ' ' * (n // 3) + s)
    for s in stars:
        result.append(s * 3)

    return result


n = int(input())
answer = draw_star(n)

for i in answer:
    print(i)