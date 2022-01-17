import heapq

def solution(scoville, K):
    h = []
    cnt = 0

    for i in range(len(scoville)):  # 힙에 데이터 저장
        heapq.heappush(h, scoville[i])

    # 음식이 2개 이상인 동안 반복
    while len(h) > 1:
        # 힙에서 첫번째 값이 k 이상이면 횟수 리턴
        if h[0] >= K:
            return cnt
        # 그게 아니면 스코빌 지수에 따라 가장 낮은 2개 음식을 섞어주고, 힙에 넣어줌, 횟수 +1
        new_food = heapq.heappop(h) + (heapq.heappop(h) * 2)
        heapq.heappush(h, new_food)
        cnt += 1

    # 반복문에서 return이 안됬다면
    if h[0] >= K:  # 마지막 음식 2개를 섞어 K값을 넘긴 경우나
        return cnt
    else:  # 모든 음식을 섞어도 안되는 경우
        return -1


#test
print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3], 11))