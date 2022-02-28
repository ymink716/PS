from itertools import combinations

def solution(line):
    coordinates = []  # 교점을 담을 리스트
    for p1, p2 in combinations(line, 2):
        a, b, e = p1
        c, d, f = p2
        # 두 직선이 일치하거나 평행인 경우 건너뛰기
        if a * d - b * c == 0:
            continue
        # 교점을 구한다
        x = (b*f - e*d) / (a*d - b*c)
        y = (e*c - a*f) / (a*d - b*c)
        # 교점이 정수라면 추가
        if int(x) == x and int(y) == y:
            coordinates.append((int(x), int(y)))

    x_list = [c[0] for c in coordinates]
    y_list = [c[1] for c in coordinates]

    # x축, y축의 최대 최소 찾아 그만큼만 순회
    min_x, max_x, min_y, max_y = min(x_list), max(x_list), min(y_list), max(y_list)
    answer = []
    for j in range(max_y, min_y - 1, -1):
        row = ""
        for i in range(min_x, max_x + 1):
            if (i, j) in coordinates:
                row += "*"
            else:
                row += "."
        answer.append(row)

    return answer


# test case
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))