def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            return binary_search(array, target, mid + 1, end)
    return None

n = int(input())  # 가게의 부품 개수
array = list(map(int, input().split()))  # 가게에 있는 전체 부품 번호들
array.sort()  # 이진탐색을 위한 정렬
m = int(input())  # 손님이 요청한 부품 개수
x = list(map(int, input().split()))  # 손님이 요청한 전체 부품 번호들

# 손님이 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

