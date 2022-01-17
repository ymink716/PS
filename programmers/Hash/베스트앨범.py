def solution(genres, plays):
    total = {}  # 장르별 플레이 횟수
    songs_by_genre = {}  # 장르 : [(고유번호, 재생횟수)...]

    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
            songs_by_genre[genres[i]].append([i, plays[i]])
        else:
            total[genres[i]] = plays[i]
            songs_by_genre[genres[i]] = [[i, plays[i]]]

    # 장르별 재생횟수 내림차순으로 Sort
    sorted_total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for (genre, total_play) in sorted_total:
        # 노래별 재생횟수 내림차순, 고유번호 오름차순 Sort
        songs_by_genre[genre].sort(key=lambda  x: (-x[1], x[0]))
        # 각 장르별 2개의 고유번호를 추가
        answer += [ i for (i, play) in songs_by_genre[genre][:2] ]

    return answer


# test
print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))