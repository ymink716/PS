for _ in range(int(input())):
    k = int(input())  # k층
    n = int(input())  # n호

    data = [i for i in range(1, n + 1)]  # 한 층의 거주자 수를 담을 리스트
    for i in range(k):
        prev = list(data)  # 이전 층의 거주자 수를 담을 리스트
        for j in range(n):
            data[j] = sum(prev[:j+1])

    print(data[-1])

