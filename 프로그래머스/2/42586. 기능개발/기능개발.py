from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    s_queue = deque(speeds)
    while queue:
        for i, q in enumerate(queue):
            queue[i] = q + s_queue[i]
        a = 0
        while queue and queue[0] > 99:
            queue.popleft()
            s_queue.popleft()
            a += 1
        if a != 0:
            answer.append(a)
    return answer