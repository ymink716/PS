import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# data를 중복 제거 후 정렬
sorted_data = sorted(list(set(data)))
# 정렬된 리스트의 인덱스 값이 좌표 압축된 결과
dic = {sorted_data[i]: i for i in range(len(sorted_data))}

for d in data:
    print(dic[d], end=" ")