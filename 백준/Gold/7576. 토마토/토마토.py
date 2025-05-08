M, N = list(map(int, input().split(' ')))

total = N * M

arr = []
q = []
visited = [[False]* M for _ in range(N)]
for i in range(N):
    line = list(map(int, list(input().split(' '))))
    for j, t in enumerate(line):
        if t == -1:
            total -= 1
        elif t == 1:  # 1이면 해당 위치 start 포인트로 저장해둠.
            q.append([i, j])
            total -= 1
    arr.append(line)
            
from collections import deque

def bfs(N, M, arr, today, visited):
    tomorrow = deque()  # 여기다가 내일 돌아야 하는 양
    seen = set()
    while today:  # 오늘 돌아야 하는 양만 딱 돌고 끝나야 함.
        x, y = today.popleft()
        visited[x][y] = True
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                if not visited[nx][ny] and (nx, ny) not in seen:
                    tomorrow.append([nx, ny])
                    seen.add((nx, ny))
    return tomorrow
                    
if total == 0:
    print(0)
else:
    days = -1
    q = deque(q)
    while q:
        q = bfs(N, M, arr, q, visited)  # 그 다음날 탐색할 토마토 위치 리스트 업데이트
        for x, y in q:
            arr[x][y] = 1  # 토마토 익음 업데이트
            total -= 1
        days += 1  # 다음날이 됩니다.
    if total != 0:
        print(-1)
    else:
        print(days)
        