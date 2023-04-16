# 결혼식

n = int(input())
m = int(input())

# 친구 관계를 담을 그래프 초기화
graph = [[] for _ in range(501)]

# 친구 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friends = set()  # 친구, 친구의 친구를 담을 셋 (중복 제거)

for p in graph[1]:  # 1번의 친구들 찾기
    friends.add(p)
    for q in graph[p]:  # 친구의 친구들 찾기
        friends.add(q)

friends = friends - {1}  # 셋에 1번이 포함될 수도 있으므로 빼주기

print(len(friends))
