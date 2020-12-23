# 주어진 시간에서부터 1초 동안 처리량을 구하는 함수
def check(s, times):
    count = 0
    start = s
    end = s + 1000
    for time in times:
        # 현재 트래픽이 주어진 1초 사이에 있으면
        if time[1] >= start and time[0] < end:
            count += 1
    return count

def solution(lines):
    times = []
    for line in lines:
        _, s, t = line.split()
        s = s.split(':')  # 시, 분, 초
        t = float(t[:-1]) * 1000  # 처리시간 밀리초로 변경
        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * 1000  # 끝시간
        start = end - t + 1  # 시작시간
        times.append([start, end])  # times 리스트에 추가 [시작시간, 끝시간]

    answer = 0
    for time in times:
        # 트래픽의 시작과 끝을 기준으로 최대 처리량 검사
        answer = max(answer, check(time[0], times), check(time[1], times))
    return answer

# test
print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
