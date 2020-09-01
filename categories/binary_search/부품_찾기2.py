# set 이용

n = int(input())  # 가게의 부품 개수
# 가게에 있는 전체 부품 번호를 입력받아 set 자료형에 기록
array = set(map(int, input().split()))

m = int(input())  # 손님이 요청한 부품 개수
x = list(map(int, input().split()))  # 손님이 요청한 전체 부품 번호들

# 손님이 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
