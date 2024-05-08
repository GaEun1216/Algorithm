
from collections import deque

move = [(1,0),(0,1),(-1,0),(0,-1)]

T = int(input())

def bfs(field, visited, path,que):
    queue = deque(que)
    while queue:
        x,y = queue.popleft()
        for dx,dy in move:
            nx, ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 or \
                        (path[nx][ny] > path[x][y] + field[nx][ny]):
                    visited[nx][ny] = 1
                    path[nx][ny] = path[x][y] + field[nx][ny]
                    queue.append((nx,ny))


for test_case in range(1,T+1):
    N = int(input())
    field = [ list(map(int,input())) for _ in range(N) ]
    visited = [[0]*N for _ in range(N) ]
    path = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((0,0))
    bfs(field, visited, path, queue)
    result = path[N-1][N-1]
    print(f"#{test_case} {result}")