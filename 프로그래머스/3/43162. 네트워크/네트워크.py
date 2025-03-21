from collections import deque

def solution(n, computers):
    answer = 0
    # 걍 대칭 생각하지말고, 찐 1인것만 내비두자.
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                arr[i].append(j)
                arr[j].append(i)
    def bfs(v, visited, arr):
        q = deque()
        if v not in visited:  # 현재 시작 노드를 한번도 방문한적이 없다면, 방문 처리하고 방문할 후보 q에 넣자.
            visited.append(v)
            q.append(v)
        while q:  # 방문할 후보가 있는 한, 계속 방문을 할건데
            target = q.popleft()  # 우선 맨 처음 방문할 곳.
            for a in arr[target]:  # 해당 방문할 시작 노드에서 해당 행을 살펴보자. 
                if a not in visited: # 무조건 이전에 방문 경험이 있는 인덱스를 또 방문하면 당연히 한 네트워크로 처리됨.
                    # 만일 니가 새로운 길을 개척하는 거라면, 
                    q.append(a)
                    visited.append(a)
        return visited
        
    # 여기서 말하는 visited는 시작 노드가 될 행 인덱스, 탐색한 행 인덱스는 집어넣기
    visited = []
    for i in range(n):
        if i not in visited:
            visited = bfs(i, visited, arr)
            answer += 1
    return answer