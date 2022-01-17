def check(array):
    for x, y, a in array:
        if a == 0:  # 기둥
            # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위 = 정상
            if y == 0 or [x - 1, y, 1] in array or [x, y, 1] in array or [x, y - 1, 0] in array:
                continue
            return False
        else:  # 보
            # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결 = 정상
            if [x, y - 1, 0] in array or [x + 1, y - 1, 0] in array or ([x - 1, y, 1] in array and [x + 1, y, 1] in array):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            # 삭제 후 불가능한 구조물이면 다시 설치
            if not check(answer):
                answer.append([x, y, a])
        else:  # 설치
            answer.append([x, y, a])
            # 설치 후 불가능한 구조물이면 제거
            if not check(answer):
                answer.remove([x, y, a])
    answer.sort()
    return answer

# test
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))