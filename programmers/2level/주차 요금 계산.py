from datetime import datetime
import math

def calculate_fee(fees, arr):
    stack = []  # 해당 차량이 주차장 안에 있는 상태인지 확인하기 위한 리스트
    t = datetime.strptime("00:00", '%H:%M')  # 주차한 시간
    while arr:
        now = arr.pop(0)  # 해당 차량의 기록을 하나 pop
        if now[1] == 'IN':  # in 인 경우
            stack.append(now)
        else:  # out인 경우
            # 스택에 있는 in 했을 때 기록을 꺼내서 둘의 차이 계산
            prev = stack.pop()
            t += (datetime.strptime(now[0], '%H:%M') - datetime.strptime(prev[0], '%H:%M'))
    if len(stack) == 1:  # 차량을 주차장에 둔 채로 하루가 경과한 경우
        now = stack.pop()
        t += (datetime.strptime("23:59", '%H:%M') - datetime.strptime(now[0], '%H:%M'))

    base_time, base_fee, unit_time, unit_fee = fees
    m = t.hour * 60 + t.minute  # 주차한 시간을 분으로 환산
    if base_time >= m:  # 기본 시간 이내인 경우
        return base_fee
    else:  # 기본 시간 초과인 경우
        return base_fee + math.ceil((m - base_time) / unit_time) * unit_fee

def solution(fees, records):
    d = dict()  # 차량번호별 출입기록을 담아둘 딕셔너리
    for r in records:
        time, car_number, history = r.split()
        try:
            d[car_number].append((time, history))
        except KeyError:
            d[car_number] = [(time, history)]

    answer = []
    # 차량번호들을 정렬하여 순회
    for n in sorted(d.keys()):
        answer.append(calculate_fee(fees, d[n]))
    return answer


# test case
print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN",
                "16:00 0202 IN",
                "18:00 3961 OUT",
                "18:00 0202 OUT",
                "23:58 3961 IN"]))
print(solution([1, 461, 1, 10],
               ["00:00 1234 IN"]))
