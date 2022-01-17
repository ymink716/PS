def solution(triangle):
    # 정답을 담을 리스트 초기화
    answer = triangle.pop()

    # 트라이앵글에 원소가 있을 때 까지 반복
    while(triangle):
        # 트라이앵글을 밑에서부터 한 줄 pop
        next = triangle.pop()
        temp = []
        # next 길이만큼 반복
        for i in range(len(next)):
            # answer가 밑에 줄, next가 위에 줄
            # 밑에 줄에서 위에 줄로 가는 경로는 next 각 요소마다 2개씩
            # next 각 요소에 가는 경로 2가지 중 최대값을 저장
            temp.append(max(next[i] + answer[i], next[i] + answer[i+1]))
        answer = temp  # 결과를 answer에 저장

    return answer[0]


# test
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))