from collections import deque

T = 10

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int,input().split())) for _ in range(100)]
    end_x = 99
    end_y = 0
    
    for i in range(100):
        if miro[99][i] == 2:
            end_y = i
    
    while end_x > 0:
        # 오른쪽
        if 0 < end_y + 1 <= 99 and miro[end_x][end_y+1] == 1:
            while 0 < end_y + 1 <= 99 and miro[end_x][end_y+1] == 1:
                end_y += 1
            end_x -= 1
        # 왼쪽
        elif 0 < end_y - 1 <= 99 and miro[end_x][end_y-1] == 1:
            while 0 < end_y - 1 <= 99 and miro[end_x][end_y-1] == 1:
                end_y -= 1
            end_x -= 1
        else:
            end_x -= 1
        
            
    print(f"#{tc} {end_y}")
