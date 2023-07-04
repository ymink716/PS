# Maaaaaaaaaze
# https://www.acmicpc.net/problem/16985

from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

boards = []
for _ in range(5):
    board = []
    for _ in range(5):
        board.append(list(map(int, input().split())))
    boards.append(board)

def rotate_board(b):
    pass