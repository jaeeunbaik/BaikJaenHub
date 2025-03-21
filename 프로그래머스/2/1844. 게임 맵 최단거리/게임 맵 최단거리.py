# BFS 문제였습니다..
from collections import deque
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y, 1))
        visited[x][y] = True
        while q:
            cur_x, cur_y, dist = q.popleft()  # 현재 위치
            if cur_x == len(maps) - 1 and cur_y == len(maps[0]) - 1: # 목적지 도달하면,
                return dist
                    
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if not visited[nx][ny] and maps[nx][ny]==1: # 이동할 수 있으면
                        q.append((nx, ny, dist + 1))
                        visited[nx][ny] = True
        if not visited[len(maps) - 1][len(maps[0]) - 1]:
            return -1
    return bfs(0,0)