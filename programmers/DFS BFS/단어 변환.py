def dfs(begin, target, words, visited):
    result = 0
    stack = [begin]
    while stack:
        top = stack.pop()
        if top == target:  # 스택에서 꺼낸 값과 타겟의 값이 같으면 리턴
            return result
        for k, word in enumerate(words):
            cnt = 0  # 비교할 두 단어의 각 글자가 몇 개나 다른지
            for i in range(len(word)):
                if top[i] != word[i]:
                   cnt += 1
            # 한글자만 다르고 방문한적 없는 단어이면
            if cnt == 1 and visited[k] == 0:
                visited[k] = 1
                stack.append(word)
        result += 1

def solution(begin, target, words):
    # target이 words 안에 없으면 0을 리턴
    if target not in words:
        return 0
    visited = [0] * len(words)  # 방문 여부
    return dfs(begin, target, words, visited)


# test
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


"""
BFS 풀이
from collections import deque

def solution(begin, target, words):
    # target이 words 안에 없는 경우
    if target not in words:
        return 0

    queue = deque([(begin, 0)])  # 큐 초기화 (시작값, depth)
    while queue:
        now, depth = queue.popleft()
        # words를 순회하면서 현재 값과 한 문자만 바꿔서 변환할 수 있는지 판별
        for word in words:
            diff = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    diff += 1
 
            if diff == 1:  # 변환 가능하다면
                if word == target:  # 변환한 단어(word)가 타겟과 같다면
                    return depth + 1  # 변환 횟수 + 1 리턴
                else :  # 그게 아니면 큐에 변환한 단어 (word, depth+1) 삽입
                    queue.append((word, depth + 1))
"""