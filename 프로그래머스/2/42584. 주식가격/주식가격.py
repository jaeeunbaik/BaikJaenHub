from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    timestamps = deque()  # 현재보다 가격이 낮은 이전 시점들
    for i, temp in enumerate(prices):  # 각 시점과 그 때의 주식 가격에 대해서
        while timestamps and prices[timestamps[-1]] > temp: # 주식 가격이 떨어지면,
            stamp = timestamps.pop()  # 시점 계속 update()
            answer[stamp] = i - stamp
        timestamps.append(i)
    
    i = len(prices) - 1
    while timestamps:
        stamp = timestamps.pop()
        answer[stamp] = i - stamp
    return answer