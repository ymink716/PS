# 게임 닉네임
# https://www.acmicpc.net/problem/16934

from collections import defaultdict
import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        current_node = self.head  # 헤드 노드부터 시작

        for char in word:  # 문자열의 문자를 하나씩 확인
            if char not in current_node.children:  # 현재 노드의 자식 중에 해당 문자가 없다면
                current_node.children[char] = Node()  # 노드를 생성, 자식 노드 추가
            current_node = current_node.children[char]  # current_node를 자식 노드로 변경
        same_nick[word] += 1  # 같은 닉네임 + 1
        current_node.word = True

    def search(self, word):
        current_node = self.head
        re_word = ''  # 반복된 문자열을 저장
        for char in word:  # 단어의 문자를 하나씩 확인
            re_word += char  # 중복 문자 추가
            if char not in current_node.children:  # 해당 문자가 현재 노드의 자식 노드에 없다면
                return re_word
            current_node = current_node.children[char]  # 현재 노드를 자식 노드로

        # 해당 단어의 문자를 모두 검색한 후 현재 노드에 단어가 있다면
        # (중복 문자열 = 전체 닉네임)
        if current_node.word:
            re_word += str(same_nick[re_word] + 1)  # 풀네임 + 같은 닉네임 수 + 1
        return re_word


n = int(input())
tree = Trie()
same_nick = defaultdict(int)  # 닉네임 중복 횟수를 저장할 딕셔너리

# 삽입 이전에 탐색을 통해 중복되는 닉네임이 있는지 확인
for _ in range(n):
    word = input().rstrip()
    print(tree.search(word))
    tree.insert(word)


