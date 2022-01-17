def solution(n, lost, reserve):
    # 학생들의 체육복 현황 초기화
    students = [1] * n
    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    for i, s in enumerate(students):
        # 보유수가 0인 학생을 기준으로
        # 왼쪽, 오른쪽 순으로 받을 수 있는 체육복이 있는지 확인
        if s != 0:
            continue
        # 기준에서 왼쪽부터 탐색해야 최적해가 나온다
        if i > 0 and students[i-1] == 2:
            students[i-1] -= 1
            students[i] += 1
        elif i < len(students)-1 and students[i+1] == 2:
            students[i+1] -= 1
            students[i] += 1

    return n - students.count(0)

# test
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))