class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 해당 노드의 문자
        self.data = data  # 문자열이 끝나는 위치를 알려주는 역할, 없을 경우 None
        self.children = {}  # 자식 노드

class Trie:
    def __init__(self):
        self.head = Node(None)  # 헤드를 빈 노드로 설정

    def insert(self, string):  # 트리를 생성
        current_node = self.head  # 헤드 노드부터 시작

        for char in string:  # 문자열의 문자를 하나씩 확인
            if char not in current_node.children:  # 현재 노드의 자식 중에 해당 문자가 없다면
                current_node.children[char] = Node(char)  # 노드를 생성, 자식 노드 추가
            current_node = current_node.children[char]  # current_node를 자식 노드로 변경
        current_node.data = string  # 문자열이 끝난 지점의 노드에 data 추가

    def search(self, string):  # 해당 문자열이 있는지 찾는 함수
        current_node = self.head  # 헤드 노드부터 시작

        for char in string:  # 문자열의 문자를 하나씩 확인
            if char in current_node.children:
                current_node = current_node.children[char]
            else:  # 현재 노드의 자식 노드 중 해당 문자에 해당하는 노드가 없다면
                return False

        if current_node.data:  # 문자열을 끝까지 탐색하여 마지막 노드에 데이터가 존재한다면
            return True
        else:  # 문자열을 끝까지 탐색하여 마지막 노드에 데이터가 없다면
            return False

    def starts_with(self, prefix):  # prefix로 시작하는 문자열을 저장한 배열 반환
        current_node = self.head
        words = []  # prefix로 시작하는 문자열을 저장할 리스트

        for p in prefix:  # prifix의 문자를 순회
            if p in current_node.children:  # 현재 노드의 자식 노드 중 해당 문자에 해당하는 노드가 존재
                current_node = current_node.children[p]  # current_node를 자식 노드로 변경
            else:  # 현재 노드의 자식 노드 중 해당 문자에 해당하는 노드가 없다면
                return None

        current_node = [current_node]  # prefix의 마지막 노드
        next_node = []  # 다음 노드를 저장할 배열
        while True:
            for node in current_node:  # 현재 노드부터 탐색
                if node.data:  # 데이터가 있다면
                    words.append(node.data)  # words 리스트에 추가
                next_node.extend(list(node.children.values()))  # 현재 노드의 자식 노드 전부를 next_node 리스트에 추가

            if len(next_node) != 0:  # 다음 노드가 존재한다면
                current_node = next_node  # 다음 노드들을 현재 노드로 설정
                next_node = []  # next_node는 비워줌
            else:  # 다음 노드가 없다면 종료
                break

        return words