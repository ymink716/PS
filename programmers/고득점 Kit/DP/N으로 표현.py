def solution(N, number):
    if N == number:
        return 1
    
    # n개의 N으로 표현할 수 있는 수들의 집합을 담을 리스트 생성
    # 1~8 까지만 확인하면 된다 (최소값이 8보다 클 수 없음)
    dp = [set() for _ in range(8)]

    for i, s in enumerate(dp, start=1):
        s.add(int(str(N) * i))   # 5, 55 ... N을 이어붙인 경우를 각 set에 저장

    # n번 set :
    # {1번 set (연산) n-1번 set} U {2번 set (연산) n-2 set} U ... {U n-1번 set (연산) 1번 set}
    # 4 = 4 | 1+3 | 2+2 | 3+1
    # 빼기, 나누기는 자리가 바뀌면 값이 바뀌므로 이렇게 해야함..
    for i in range(1, 8):  # i에 대해서 2~8 순회
        for j in range(i):  # j에 대해서 0~(i-1) 순회하면서
            for op1 in dp[j]:  # j개를 사용해서 만든 수들의 집합 dp[j]를 순회
                for op2 in dp[i-j-1]:  # i-j-1개를 사용해서 만든 수들의 집합 dp[i-j-1]를 순회
                    # 사칙연산한 결과 값을 dp[i]에 추가
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        # number가 dp[i]에 존재한다면 i+1을 리턴
        if number in dp[i]:
            answer = i + 1
            break
        else:
            answer = -1

    return answer


# test
print(solution(5, 12))
print(solution(2, 11))
