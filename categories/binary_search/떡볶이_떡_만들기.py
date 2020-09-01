n, m = list(map(int, input().split(' ')))  # 떡의 개수, 요청한 떡의 길이
array = list(map(int, input().split()))  # 각 떡의 높이

start, end = 0, max(array)  # 이진탐색을 위한 시작점, 끝점
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1

print(result)
