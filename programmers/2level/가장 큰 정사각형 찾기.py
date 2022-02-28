def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                #
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    answer = 0
    for b in board:
        temp = max(b)
        answer = max(answer, temp)

    return answer ** 2


# test
print(solution([[0, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1],
                [1, 1, 1, 1]]))


