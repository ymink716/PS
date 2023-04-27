# 공주님의 정원

import sys
input = sys.stdin.readline

n = int(input())  # 꽃들의 개수

flowers = []  # (꽃이 피는 날짜, 꽃이 지는 날짜)
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    flowers.append((start_m * 100 + start_d, end_m * 100 + end_d))  # 월에 100을 곱해서 일에 더해줌

flowers.sort()  # 꽃이 피는 날짜, 꽃이 지는 날짜 순으로 오름차순 정렬
end_date = 301  # 정원의 마지막 꽃이 피는 날짜
count = 0  # 심은 꽃의 개수

while flowers:  # 더 이상 확인할 꽃이 없을 때까지
    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상 or
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜와 이어지지 않는 경우
    if end_date >= 1201 or flowers[0][0] > end_date:
        break

    temp = -1  # 꽃이 피는 날짜가 end_date 이전이면서 가장 느리게 지는 꽃의 날짜
    for _ in range(len(flowers)):  # 꽃들을 순회하면서
        if flowers[0][0] <= end_date:  # 꽃이 피는 날짜가 end_date 이전일 때
            if temp <= flowers[0][1]:  # 가장 느리게 지는 꽃을 확인
                temp = flowers[0][1]
            flowers.remove(flowers[0])  # 확인한 꽃을 제거
        else:
            break

    end_date = temp  # end_date 갱신
    count += 1  # 심은 꽃의 개수 +1

if end_date < 1201:  # 마지막 꽃의 지는 날짜가 12월 1일 보다 작으면 계속 피어 있던 것이 아님
    print(0)
else:
    print(count)