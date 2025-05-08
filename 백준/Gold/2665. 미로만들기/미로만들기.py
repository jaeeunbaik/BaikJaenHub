N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))
    
    
    
from collections import deque
# visited = [[[False] for i in range(N)] for j in range(N)]
inf = 1000
visited = [[-1] * N for _ in range(N)]
start = [0, 0]
        
def bfs(arr, loc, visited):
    q = deque([loc])
    visited[loc[0]][loc[1]] = 0  # 시작점 큐에 넣기
    while q:  # 큐에 남아있으면 계속 돌아
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return visited[-1][-1]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            # 방문한 적 없고, 지도에 있는 위치면 큐에 넣고 이동함.
            if nx > -1 and nx < N and ny > -1 and ny < N and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:  # 새로 이동하는 위치가 흰 색 방이면 이전 black 값 유지
                    q.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                     
print(bfs(arr, start, visited))