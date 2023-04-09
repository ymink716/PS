# List of Unique Numbers

n = int(input())
array = list(map(int, input().split()))

answer = 0
checked = [False] * 100001  # 이미 나온 숫자인지 확인하는 배열
start, end = 0, 0  # 투 포인터


while start !=n and end != n:  # start = end = n이 될 때까지 반복
    if not checked[array[end]]:  # end 지점이 아직 나오지 않은 수인 경우
        checked[array[end]] = True  # end 지점 체크
        end += 1  # end값 전진
        answer += end - start  # end를 포함하여 만들 수 있는 수열의 개수
    else:  # end 지점이 이미 나온 수인 경우
        checked[array[start]] = False  # start 지점의 값 체크 해제
        start += 1  # start값 전진

print(answer)