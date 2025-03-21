# 한 알파벳씩 돌아가며 검사하기
def check(word1, word2):
    diff = 0
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            diff += 1
    if diff == 1:
        return True
    else: return False

# 이놈은 무조건 BFS다. 최소거리구하는거자나
from collections import deque
def solution(begin, target, words):
    visited = {}
    for w in words:
        visited[w] = False
    visited[begin] = False
    def bfs():
        answer = 0
        q = deque()
        q.append((begin, 0))
        while q:
            cur, num = q.popleft()
            visited[cur] = True
            if cur == target:
                return num
            for w in words:
                if check(cur, w) and not visited[w]:
                    q.append((w, num + 1))
        if cur != target:
            return 0
    return bfs()