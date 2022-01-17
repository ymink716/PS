def solution(name):
    # 각 자리의 상하 조작의 최소값 구하기 : char-'A'와 'Z'-char+1 중에서 작은 값을 고른다
    array = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]

    answer = 0
    index = 0
    while True:
        answer += array[index]  # 현재 위치 문자의 변경 횟수에 추가
        array[index] = 0  # 변경되었으므로 0으로 바꿔준다

        # 모든 조작이 끝난 경우
        if sum(array) == 0:
            break

        # 좌우 조작의 최소 횟수 구하기 : A와 이미 변경된 값 반대쪽으로
        # 왼쪽 오른쪽에서 0을 만나는 경우(A이거나 이미 변경됨)의 최소값을 구한다
        left, right = 1, 1
        while array[index - left] == 0:
            left += 1
        while array[index + right] == 0:
            right += 1

        # 왼쪽이 작은 경우, 왼쪽으로 간 횟수를 더해주고 인덱스를 왼쪽으로 옮김
        if left < right:
            answer += left
            index -= left
        # 그게 아니면 오른쪽으로 간 횟수를 더해주고 인덱스를 오른쪽으로 옮김
        else:
            answer += right
            index += right

    return answer


# test
print(solution('JEROEN'))
print(solution('JAN'))