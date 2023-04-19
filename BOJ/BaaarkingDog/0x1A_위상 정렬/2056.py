# 작업

n = int(input())
graph = {}
times = [0] * (n + 1)

for i in range(1, n + 1):
    array = list(map(int, input().split()))
    times[i] = array[0]  # 해당 작업에 걸리는 시간
    if array[1] == 0:
        continue
    for j in array[2:]:  # 해당 작업에 필요한 선행 작업들
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]

# 순회하면서 해당 작업에 필요한 선행 작업 중 가장 늦게 끝나는 작업의 시간을 더해줌
for i in range(1, n + 1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])

        times[i] += time

print(max(times))  # 작업에 필요한 시간들 중 최댓값 출력




