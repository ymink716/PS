k = int(input())  # 1m^2 당 참외 수
array = []  # [방향, 길이] 값을 저장할 배열
for i in range(6):
    d, l = map(int, input().split())
    array.append([d, l])

max_w, max_h = 0, 0  # 가장 긴 가로 길이, 가장 긴 세로 길이
max_w_idx, max_h_idx = 0, 0  # 가장 긴 가로와 세로의 인덱스

for i in range(len(array)):
    if array[i][0] in [1, 2]:  # 동, 서 -> 가로
        if max_w < array[i][1]:  # 가로 길이 최대값 갱신
            max_w_idx = i
            max_w = array[i][1]
    elif array[i][0] in [3, 4]:  # 남, 북 -> 세로
        if max_h < array[i][1]:  # 세로 길이 최대값 갱신
            max_h = array[i][1]
            max_h_idx = i

# 작은 사각형의 가로 : 가장 긴 세로 변의 양 옆에 존재하는 두 가로변의 차이
# 작은 사각형의 세로 : 가장 긴 가로 변의 양 옆에 존재하는 두 세로변의 차이
small_w = abs(array[(max_h_idx - 1) % 6][1] - array[(max_h_idx + 1) % 6][1])
small_h = abs(array[(max_w_idx - 1) % 6][1] - array[(max_w_idx + 1) % 6][1])

print((max_w * max_h - small_w * small_h) * k)  # (큰 사각형 넓이 - 작은 사각형 넓이) * k