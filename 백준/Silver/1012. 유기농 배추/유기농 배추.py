from collections import deque

def dfs(M, N, arr, visited, start):
    q = deque([start])
    while q:
        x, y = q.pop()
        visited[x][y] = True
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N  and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append([nx, ny])
    return 1
T = int(input())

answer = [0] * T
for t in range(T):
    M, N, K = list(map(int, input().split(' ')))
    arr = [[0]* N for m in range(M)]
    for k in range(K):
        x, y = list(map(int, input().split(' ')))
        arr[x][y] = 1

    visited = [[False]* N for m in range(M)]
    for m in range(M):
        for n in range(N):
            if not visited[m][n] and arr[m][n] == 1:
                answer[t] += dfs(M, N, arr, visited, [m, n])
for a in answer:
    print(a)