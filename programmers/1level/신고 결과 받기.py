from collections import Counter

def solution(id_list, report, k):
    from_to = dict()  # 신고한 사용자 : [신고 당한 사용자들...]
    for id in id_list:
        from_to[id] = []

    reported_users = []  # 신고 당한 사용자들 전체
    for r in report:
        a, b = r.split()
        if b not in from_to[a]:
            from_to[a].append(b)
            reported_users.append(b)

    c = Counter(reported_users)
    suspended_users = []  # 정지된 사용자 목록
    for id in c.keys():
        if c[id] >= k:
            suspended_users.append(id)

    answer = []
    for a in id_list:  # 전체 사용자들을 순회하면서
        count = 0
        for b in from_to[a]:  # 각 사용자들이 신고한 유저들을 순회
            # 해당 유저가 정지되었으면 count +1
            if b in suspended_users:
                count += 1
        answer.append(count)

    return answer



# test
print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2))
print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3))