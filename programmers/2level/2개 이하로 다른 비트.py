def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            y = '0' + bin(n)[2:]
            i = y.rfind('0')
            y = list(y)
            y[i] = '1'
            y[i+1] = '0'
            answer.append(int(''.join(y), 2))
    return answer


# test case
print(solution([2, 7]))