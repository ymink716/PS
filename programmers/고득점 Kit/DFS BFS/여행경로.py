def solution(tickets):
    graph = dict()  # 그래프 생성

    # 'start':[end, end]
    for (start, end) in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    # 알파벳 순서상 맨 앞 값을 먼저 꺼내오기 위해 value 값을 역순으로 정렬
    for key in graph.keys():
        graph[key].sort(reverse=True)

    stack = ["ICN"]  # 스택 초기화
    path = []

    while stack:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:  # top으로 시작하는 경로가 없을 경우
            path.append(stack.pop())  # path에 저장
        else:  # top을 시작점으로 하는 end 값 중 마지막 값을 빼서 stack에 저장
            stack.append(graph[top].pop())

    return path[::-1]  # 끝에서부터 저장되었으므로 리스트를 뒤집어 리턴한다.


# test
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
