from collections import deque

def solution(arr):
    answer = []
    
    queue = deque()
    for a in arr:
        queue.appendleft(a)
    answer.append(queue.pop())
    while queue:
        q = queue.pop()
        if q != answer[-1]:
            answer.append(q)
    return answer