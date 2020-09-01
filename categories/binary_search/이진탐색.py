# 재귀
def binary_search(array, target, start, end):
    if start > end:
        return None
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

# 반복문
#def binary_search(array, target, start, end):
#    while start <= end:
#        mid = (start + end) // 2
#        # 찾은 경우 중간점 인덱스 반환
#        if array[mid] == target:
#            return mid
#        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#        elif array[mid] > target:
#            return binary_search(array, target, start, mid - 1)
#        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
#        else:
#            return binary_search(array, target, mid + 1, end)
#    return None


n, target = list(map(int, input().split()))  # 원소의 개수, 타겟
array = list(map(int, input().split()))  # 전체 원소

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)