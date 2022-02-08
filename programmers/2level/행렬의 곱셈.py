def solution(arr1, arr2):
    # x 곱셈 결과의 행의 개수, y 곱셈 결과의 열의 개수, z 곱해질 때 반복될 수
    x, y, z = len(arr1), len(arr2[0]), len(arr1[0])
    answer = [[0] * y for _ in range(x)]  # 결과 배열 초기화

    for i in range(x):
        for j in range(y):
            temp = 0
            for k in range(z):
                temp += arr1[i][k] * arr2[k][j]
            answer[i][j] = temp
    return answer


# test case
print(solution(
    [[1, 4],
     [3, 2],
     [4, 1]],
    [[3, 3],
     [3, 3]]))
print(solution(
    [[2, 3, 2],
     [4, 2, 4],
     [3, 1, 4]],
    [[5, 4, 3],
     [2, 4, 1],
     [3, 1, 1]]))