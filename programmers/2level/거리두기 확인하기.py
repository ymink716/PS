from itertools import combinations

def solution(places):
    answer = []
    for place in places:  # 각 대기실을 순회
        array, result = [], 1
        for i in range(len(place)):  # 대기자 좌표 찾기
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    array.append([i, j])

        if len(array) <= 1:  # 대기자가 1명 이하인 경우
            answer.append(1)
            continue

        for a, b in combinations(array, 2):
            m = abs(a[0] - b[0]) + abs(a[1] - b[1])  # 맨허튼 거리
            if m == 1:  # 맨허튼 거리가 1이면 거리두기를 지키지 않음
                result = 0
                break
            elif m == 2:  # 맨허튼 거리가 2일 때
                # 가로로 마주한 경우
                if a[0] == b[0] and place[a[0]][(a[1] + b[1]) // 2] == 'O':
                    result = 0
                    break
                # 세로로 마주한 경우
                elif a[1] == b[1] and place[(a[0] + b[0]) // 2][a[1]] == 'O':
                    result = 0
                    break
                # 대각선으로 마주한 경우
                elif place[a[0]][b[1]] == 'O' or place[b[0]][a[1]] == 'O':
                    result = 0
                    break
        answer.append(result)

    return answer


# test
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))