N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

from collections import deque
visited = [[False] * N for _ in range(N)]

def bfs(start, arr, visited):
    q = deque([start])
    total = 0
    while q:
        x, y = q.popleft()
        total += 1
        visited[x][y] = True
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if nx > -1 and nx < N and ny > -1 and ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
                if [nx, ny] not in q:
                    q.append([nx, ny])
    return total
            
num = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:  # 1이면서 방문 안 한 곳을 발견하면 거기서 시작점으로 bfs 탐색을 함.
            num.append(bfs([i, j], arr, visited))
num.sort()
print(len(num))
for n in num:
    print(n)