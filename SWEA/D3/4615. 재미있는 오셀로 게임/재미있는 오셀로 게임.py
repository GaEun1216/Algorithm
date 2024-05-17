move = [(1,0),(1,1),(1,-1),(0,-1),(0,1),(-1,1),(-1,0),(-1,-1)]
def start(x,y):
    key = game[x][y]
    key2 = 2 if game[x][y] == 1 else 1
    for dx,dy in move:
        que = []
        nx , ny = x+dx, y+dy
        while 0 <= nx < N and 0 <= ny < N:
            if game[nx][ny] == key:
                if que:
                    for xx,yy in que:
                        game[xx][yy] = key
                break
            elif game[nx][ny] == key2:
                que.append((nx,ny))
                nx += dx
                ny += dy
            else:
                break

T = int(input())
for test_case in range(1, T + 1):
    N, M =map(int,input().split())
    result = 0
    # white : 2 , Black : 1
    game = [[0]*N for _ in range(N)]
    # white
    game[N//2][N//2] = game[N//2-1][N//2-1] = 2
    # black
    game[N//2-1][N//2] = game[N//2][N//2-1] = 1
    for i in range(M):
        x,y,color = map(int,input().split())
        x,y = x-1,y-1
        game[x][y] = color
        start(x,y)

    black = white = 0
    for i in range(N):
        for j in range(N):
            if game[i][j] == 1:
                black += 1
            elif game[i][j] == 2:
                white += 1
    print(f"#{test_case} {black} {white}")


