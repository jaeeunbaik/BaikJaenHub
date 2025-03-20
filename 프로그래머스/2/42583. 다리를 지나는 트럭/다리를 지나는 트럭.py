from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    temp = deque([0]*bridge_length)
    current_weight = 0
    
    while truck_weights: # 다리 위에 트럭이 없을 때까지
        # 만약에 올릴게 있고, 더 올라와도 되면, 올립니다. 
        answer += 1
        current_weight -= temp.popleft()
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            temp.append(truck_weights.popleft())
        # 올릴 수 없다면, 그냥 다리를 건너게 둡니다.
        else:
            temp.append(0)
    answer += bridge_length
    return answer