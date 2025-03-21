import heapq as hq
def solution(operations):
    answer = []
    for o in operations:
        if o.startswith('I '):
            hq.heappush(answer, int(o[2:]))
        elif answer and o == 'D 1':
            answer.sort()
            answer.pop()
        elif answer and o == 'D -1':
            hq.heappop(answer)
    if answer:
        answer.sort()
        return [answer[-1], answer[0]]
    else:
        return [0, 0]