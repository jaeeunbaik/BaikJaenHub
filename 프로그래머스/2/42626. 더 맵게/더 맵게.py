import heapq
def solution(scoville, K):
    answer = 0
    # heap을 생성한 다음, 루트 노드와 그 다음으로 작은 노드 반환, 새로운 음식, heap 정렬, 반복
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville)>1:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + 2 * min2
        heapq.heappush(scoville, new)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer