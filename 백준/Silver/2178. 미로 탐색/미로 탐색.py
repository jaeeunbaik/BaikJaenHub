N, M  = list(map(int, input().split()))
arr = [list(map(int, list(input()))) for _ in range(N)]
# 조건? 다음 칸 값이 1, 맵 안에 위치, 방문 기록으로 되돌아 가는 것 방지, 
from collections import deque

visited = [[-1] * M for i in range(N)]
def bfs():
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return visited[-1][-1]
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx > -1 and nx < N and ny > -1 and ny < M and visited[nx][ny] == -1 and arr[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
# bfs()
print(bfs())