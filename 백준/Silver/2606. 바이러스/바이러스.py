N = int(input())
M = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(M):
    i, j = list(map(int, input().split(' ')))
    arr[i-1][j-1] = 1
    arr[j-1][i-1] = 1
# print(arr)
visited = [False for _ in range(N)]

from collections import deque
def bfs():
    q = deque([0])
    total = -1
    visited[0] = True
    while q:
        computer = q.popleft()
        total += 1
        visited[computer] = True
        for i, a in enumerate(arr[computer]):
            if computer != i and a == 1 and not visited[i] and i not in q:
                q.append(i)
    return total
print(bfs())