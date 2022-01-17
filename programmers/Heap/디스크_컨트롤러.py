import heapq

def solution(jobs):
    jobs.sort()  # 리스트 Sort (요청 시점, 소요 시간)순 오름차순
    job_count = len(jobs)  # 작업의 총 개수
    working_hours = 0  # 작업에 걸린 시간
    time = jobs[0][0]  # 경과 시간
    h = []  # 대기 중인 작업들을 담을 heapq

    while jobs:
        (request, cost) = jobs.pop(0)  # 작업 리스트에서 첫 번째 값을 꺼내 옴 (요청시간, 소요시간)
        time += cost  # 경과 시간에 현재 작업의 소요시간을 더해줌
        working_hours += (time - request)  # 작업에 걸린 시간 += (경과 시간 - 요청 시간)

        # jobs가 비어있지 않고 jobs 첫번째 요소의 요청시간이 경과시간보다 작을 때
        while jobs and jobs[0][0] < time:
            (request, cost) = jobs.pop(0)  # jobs의 첫번째 요소를 꺼내
            heapq.heappush(h, (-cost, request))  # 최대힙으로 저장

        # heapq에 요소가 있는 동안
        while h:
            # h에서 첫번째 요소를 꺼내 jobs에 첫번째로 저장
            # cost의 최대값이 먼저 나오므로
            # jobs에는 cost의 최소값이 0번째에 있게 된다
            (cost, request) = heapq.heappop(h)
            jobs.insert(0, [request, -cost])

    return working_hours // job_count


# test
print(solution([[0, 3], [1, 9], [2, 6]]))