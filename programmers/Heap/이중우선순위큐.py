import heapq

def solution(operations):
    max_h = []  # 최대 Heap
    min_h = []  # 최소 Heap

    for op in operations:
        # 주어진 숫자 삽입
        if op.startswith("I"):
            _, num = op.split()
            heapq.heappush(min_h, int(num))
            heapq.heappush(max_h, -int(num))  # 최대힙은 -로 값을 넣고, 빼고 나서 -를 붙여 값을 원래대로
        # 최소값 삭제
        elif op == 'D -1' and len(max_h) != 0:
            min_value = heapq.heappop(min_h)
            max_h.remove(-min_value)
        # 최대값 삭제
        elif op == 'D 1' and len(max_h) != 0:
            max_value = -heapq.heappop(max_h)
            min_h.remove(max_value)

    if max_h:
        return [-heapq.heappop(max_h), heapq.heappop(min_h)]
    else:
        return [0, 0]

# test
print(solution(["I 16","D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))