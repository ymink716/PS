def solution(sizes):
    w_list, h_list = [], []

    for w, h in sizes:
        if w >= h:
            w_list.append(w)
            h_list.append(h)
        else:
            w_list.append(h)
            h_list.append(w)

    return max(w_list) * max(h_list)


# test
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))