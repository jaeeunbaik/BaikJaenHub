# DFS : 깊이 우선 탐색, stack | list
## 다음 숫자를 더하거나 빼거나 , target이랑 계속 비교. 그러면 재귀 함수는 다음숫자를 더하거나 뺀다, 
## 재귀함수는 (현재 인덱스, 지금까지합, 숫자리스트, 타겟을 받아야 함.)

def dfs(idx, total, numbers, target):
    # dfs 종료 시점: 이
    if idx == len(numbers):
        if total == target:
            return 1
        else: return 0
    add_n = dfs(idx + 1, total + numbers[idx], numbers, target)
    sub_n = dfs(idx + 1, total - numbers[idx], numbers, target)
    
    return add_n + sub_n

def solution(numbers, target):
    
    return dfs(0, 0, numbers, target)        
    