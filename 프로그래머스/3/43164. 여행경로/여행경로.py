# dfs로 구현하겠습니다.
# 재귀적으로 수행할 동작 : 현재 목적지와 동일한 출발지의 항공권 찾기
# 재귀함수 종료 조건 : 모든 항공권 사용 시 
# 재귀함수 입력 : 현재 목적지
from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for s, d in tickets:
        graph[s].append(d)
    for key in graph:
        graph[key].sort(reverse=True)
    
    def dfs(curr):
        while graph[curr]:
            n_dest = graph[curr].pop()
            dfs(n_dest)
        answer.append(curr)
    dfs('ICN')
        
    return answer[::-1]