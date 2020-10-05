n = int(input())  # 드래곤 커브의 개수

#    우, 상, 좌, 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())  # x좌표, y좌표, 방향, 세대
    graph[y][x] = 1  # 초기 좌표 1로 갱신
    directions = [d]  # 방향 정보를 담을 리스트
    # g 세대의 방향 정보 얻기
    for i in range(1, g + 1):
        # 다음 세대 방향 : [현재 세대 방향] + [(현재 세대 방향 역순) + 1]
        temp = list(directions)
        temp.reverse()
        temp = [(x+1) % 4 for x in temp]
        directions.extend(temp)
    # 해당 방향으로 이동 후 좌표값 1로 갱신
    for direction in directions:
        x = x + dx[direction]
        y = y + dy[direction]
        graph[y][x] = 1

answer = 0
for i in range(100):
   for j in range(100):
       if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
           answer += 1
print(answer)
