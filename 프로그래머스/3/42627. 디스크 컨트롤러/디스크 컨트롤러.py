from collections import deque
import heapq
def solution(jobs): # jobs는 (요청 시점, 작업 시간) 큐, waiting은 heap
    answer = 0
    cur_time = 0
    n = len(jobs)
    i = 0
    
    jobs = sorted(jobs)
    waiting = []
    while i < n or waiting:  # 작업이 남아있으면, 
        # 대기 큐 업데이트, 남은 작업이 있고, 요청시각이 되면
        while i < n and jobs[i][0] <= cur_time:  # 요청시각되거나, 지금 요청시각 지났으면(이미 올라와있는 상태다. 어차피 그 동안에는 올라와도 뭘못하니게) 다올림. 
            heapq.heappush(waiting, (jobs[i][1], jobs[i][0]))
            i += 1
        if waiting and waiting[0][1] <= cur_time:
            p, c = heapq.heappop(waiting)
            answer += cur_time + p - c  # 반환 시간: 작업 시작 + 작업하는데 걸리는
            cur_time += p
        elif jobs: # 대기리스트에 아무것도 없고, 붕 뜬 상황, 다음 작업 시작할 수 있는 시간으로 이동
            cur_time = jobs[i][0]
    return answer // n  # (3 + 9 + 18) // 3 == 10