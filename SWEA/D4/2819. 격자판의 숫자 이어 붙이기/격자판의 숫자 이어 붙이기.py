#2819
from collections import deque
move = [(1,0),(0,1),(-1,0),(0,-1)]
length = 4
T = int(input())

def dfs(x,y,result):
    if x < 0 or y < 0 or x >= length or y >= length:
        return
    result += save[x][y]
    if len(result) == 7:
        answer.append(result)
        return
    for dx,dy in move:
        dfs(x+dx,y+dy,result)



for tc in range(1,T+1):
    save = [list(map(str,input().split())) for _ in range(4)]
    answer = []
    for x in range(length):
        for y in range(length):
            dfs(x,y,"")
    answer = list(set(answer))
    print(f"#{tc} {len(answer)}")